# CRUD ( EACH TABLE IN DATABASE USING PYTHON )


import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=harshit\\SQLEXPRESS;'
    'DATABASE=Finance_DB;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

class manager :
    # FUNCTION : Read or Show the Table Data


    def read_tables(self,table):
        cursor.execute(f"SELECT * FROM {table}")
        w=1
        for i in cursor.fetchall():
            print(f"Row number {w} :")
            print(i)
            print('')
            w+=1

    # FUNCTION : Insert the new data in Table
    def insert_tables(self,table,columns,values):
        x=",".join(['?']*len(values))
        cursor.execute(f"INSERT INTO {table} ({','.join(columns)}) VALUES({x})",values)
        conn.commit()

    

    # FUNCTION : UPDATE DATA IN TABLES ->
    def update_Tables(self,table,column,value,column2,chvalue):
        try:
            cursor.execute(f"UPDATE {table} SET {column} =? WHERE {column2} = ? ",(value,chvalue))
            conn.commit()
        except Exception as err:
            print(" Error->",err)
            

    # FUNCTION : DELETION OF DATA IN TABLES ->
    def delete_Rows(self,table,column,value):
        try:
            cursor.execute(f"DELETE FROM {table} WHERE {column}=?",(value,))
            conn.commit()
        except Exception as err:
            print(" Error->",err)
      


   
    

