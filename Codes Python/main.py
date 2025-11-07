import pyodbc
import pandas as pd 
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from chart import Chart
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=harshit\\SQLEXPRESS;'
    'DATABASE=Finance_DB;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

class manager :
    def __init__(self):
        pass


    def read_tables(self,table):
        try:
          que=f"SELECT * FROM {table}"
          df=pd.read_sql(que,conn)
          print(df.to_string(index=False))
          return df
        except Exception as ee:
           print("Error->",ee)
            
            
    def insert_tables(self,table,columns,values):
        try:
            x=",".join(['?']*len(values))
            cursor.execute(f"INSERT INTO {table} ({','.join(columns)}) VALUES({x})",values)
            conn.commit()
        except Exception as ee:
            print("Error->",ee)

    def update_Tables(self,table,column,value,column2,chvalue):
        try:
            cursor.execute(f"UPDATE {table} SET {column} =? WHERE {column2} = ? ",(value,chvalue))
            conn.commit()
        except Exception as err:
            print(" Error->",err)

    def bulk_insert(self,table,path):
        try:
          que=f'''BULK INSERT {table} FROM '{path}' WITH (FIRSTROW=2,FIELDTERMINATOR=',',TABLOCK);'''
          cursor.execute(que)
          conn.commit()
        except Exception as ee :
          print("Error->", ee)
            

    
    def delete_Rows(self,table,column2,value):
        try:
            cursor.execute(f"DELETE FROM {table} WHERE {column2}=?",(value,))
            conn.commit()
        except Exception as err:
            print(" Error->",err)



class GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700")
        self.root.title("💰Finance Tracker")
        self.root.config(bg="#000000")  
        self.mng = manager()
        self.mode=None
        self.ch=Chart()

       
        tk.Label(root,text="💰 Finance Tracker 💰 ",font=("Segoe UI", 22, "bold"),fg="#00adb5",bg="#1e1e1e",pady=9).pack(fill="x")
        
       
        self.buttonsframe=tk.Frame(root,bg="#111010")
        self.buttonsframe.pack(pady=10)

        # BUttons ->

        #Read Button
        readbutton = tk.Button(self.buttonsframe,text=" 📖 Read Table",command=self.read_table,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        readbutton.grid(row=0, column=0, padx=15, pady=5)
         
        #Update BUtton
        updatebutton=tk.Button(self.buttonsframe,text="🛠️ Update Table",command=self.update_table,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        updatebutton.grid(row=0,column=1,padx=15, pady=5)
         
         #Insert Button
        insertbutton=tk.Button(self.buttonsframe,text="➕ Insert Data",command=self.insert_rows,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        insertbutton.grid(row=0,column=2, padx=15, pady=5)
         
         #Delete Button
        deletebutton=tk.Button(self.buttonsframe,text="♻️ Delete Rows",command=self.delete_rows,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        deletebutton.grid(row=0,column=3, padx=15, pady=5)
         # Bulk Button
        bulkbutton=tk.Button(self.buttonsframe,text="✖️ Bulk Insert ",command=self.bulk_insert,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        bulkbutton.grid(row=0,column=4,padx=15, pady=5)
        # monthly Income and expense chart button
        chartbutn=tk.Button(self.buttonsframe,text="📈Show charts ",command=self.prepmonth,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        chartbutn.grid(row=0,column=5,padx=15, pady=5)
        # account_type button
        acbutton=tk.Button(self.buttonsframe,text="🖥️Show type",command=self.bnktype,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        acbutton.grid(row=1,column=0,padx=15, pady=5)
        #month wise expense button
        mnthbutn=tk.Button(self.buttonsframe,text="▶️Expense line",command=self.mnthwise_expense,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        mnthbutn.grid(row=1,column=1,padx=15, pady=5)
        #Top 5 category expense wise 
        catbutn=tk.Button(self.buttonsframe,text="🔝5️⃣Category",command=self.top5,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        catbutn.grid(row=1,column=2,padx=15, pady=5)
        
        self.input_container = tk.Frame(root, bg="#F3E7E7")
        self.input_container.pack(pady=10, fill="x")

        # Frames
        self.table_frame= tk.Frame(self.input_container, bg="#000000", bd=2)
        self.column_frame=tk.Frame(self.input_container, bg="#000000", bd=2)
        self.value_frame=tk.Frame(self.input_container, bg="#000000", bd=2)
        self.column2_frame=tk.Frame(self.input_container, bg="#000000",  bd=2)
        self.chvalue_frame=tk.Frame(self.input_container,bg="#000000",bd=2)
        self.path_frame=tk.Frame(self.input_container,bg="#000000",bd=2)
        
        # Table Frame
        tk.Label(self.table_frame,text=" 📊 Table Name->",font=("Arial", 13,'bold'),fg="#eeeeee",bg="#080808").pack(side="left", padx=10, pady=10)
        self.tbentry = tk.Entry(self.table_frame,width=40, font=("Consolas", 11), bg="#ffffff", fg="#000000", insertbackground="black", relief="solid", bd=2)
        self.tbentry.pack(side="left", padx=10, pady=10)
        
        # Column Frame
        tk.Label(self.column_frame,text="🆑 Column Name->",font=("Arial",13,'bold'),fg="#eeeeee",bg="#050505").pack(side="left", padx=10, pady=10)
        self.centry=tk.Entry(self.column_frame,width=40,font=('Consolas',11),bg='#ffffff',fg="#9C1818", insertbackground="black", relief="solid", bd=2)
        self.centry.pack(side="left", padx=10, pady=10)
        
        # Value Frame
        tk.Label(self.value_frame,text="📈 New Value->",font=("Arial",13,'bold'),fg="#eeeeee",bg="#0F0F0F").pack(side="left", padx=10, pady=10)
        self.vntry=tk.Entry(self.value_frame,width=40,font=("Consolas",11),bg='#ffffff',fg="#000000", insertbackground="black", relief="solid", bd=2)
        self.vntry.pack(side="left", padx=10, pady=10)
        
        # Column2 Frame (WHERE clause)
        tk.Label(self.column2_frame,text="🔍 WHERE Column->",font=("Arial",13,'bold'),fg="#eeeeee",bg="#000000").pack(side="left", padx=10, pady=10)
        self.c2entry=tk.Entry(self.column2_frame,width=40,font=("Consolas",11),bg='#ffffff',fg="#000000", insertbackground="black", relief="solid", bd=2)
        self.c2entry.pack(side="left", padx=10, pady=10)
        
        # CHValue Frame (WHERE value)
        tk.Label(self.chvalue_frame,text="🎯 WHERE Value->",font=("Arial",13,'bold'),fg="#eeeeee",bg="#0A0A0A").pack(side="left", padx=10, pady=10)
        self.chventry=tk.Entry(self.chvalue_frame,width=40,font=("Consolas",11),bg='#ffffff',fg="#000000", insertbackground="black", relief="solid", bd=2)
        self.chventry.pack(side="left", padx=10, pady=10)

        # path Frame
        tk.Label(self.path_frame,text="🛣️Path->",font=("Arial",13,'bold'),fg="#eeeeee",bg="#0A0A0A").pack(side="left", padx=10, pady=10)
        self.bentry=tk.Entry(self.path_frame,width=40,font=("Consolas",11),bg='#ffffff',fg="#000000", insertbackground="black", relief="solid", bd=2)
        self.bentry.pack(side="left", padx=10, pady=10)
        
        self.runbutton = tk.Button(self.root,text="🏃 Run",command=self.run_action,font=("Segoe UI", 13, "bold"),bg="#760da7",fg="black", bd=5, padx=20, pady=10) 
        self.runbutton.pack(pady=10)

        text_frame = tk.Frame(root, bg="#970000")
        text_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.output = tk.Text(text_frame,width=125,height=15,bg="#0f0f0f",fg="#00ffcc",insertbackground="white",font=("Consolas", 10),relief="flat")
        self.output.pack(fill="both", expand=True)

       
    #Functions->

    def hides(self):
        func= (self.table_frame, self.column2_frame, self.column_frame, self.value_frame, self.chvalue_frame,self.path_frame)
        for f in func:
            f.pack_forget()

    def read_table(self):
        self.hides()
        self.mode ='read'
        self.table_frame.pack(pady=5, padx=10)
        

    def update_table(self):
        self.hides()
        self.mode='update'
        self.table_frame.pack(pady=5, padx=10)
        self.column_frame.pack(pady=5, padx=10)
        self.value_frame.pack(pady=5, padx=10)
        self.column2_frame.pack(pady=5, padx=10)
        self.chvalue_frame.pack(pady=5, padx=10)

    def insert_rows(self):
        self.hides()
        self.mode='insert'
        self.table_frame.pack(pady=5, padx=10)
        self.column_frame.pack(pady=5, padx=10)
        self.value_frame.pack(pady=5, padx=10)

    def delete_rows(self):
        self.hides()
        self.mode='delete'
        self.table_frame.pack(pady=5, padx=10)
        self.column2_frame.pack(pady=5, padx=10)
        self.chvalue_frame.pack(pady=5, padx=10)

    def bulk_insert(self):
       self.hides()
       self.mode='bulk'
       self.table_frame.pack(pady=5,padx=10)
       self.path_frame.pack(padx=5,pady=10)


    def run_action(self):
     if self.mode == 'read':
        self.run_read()
     elif self.mode == 'update':
        self.run_update()
     elif self.mode == 'insert':
        self.run_insert()
     elif self.mode == 'delete':
        self.run_delete()
     elif self.mode=='bulk':
        self.run_bulk()

    def run_read(self):
     table = self.tbentry.get().strip()
     data = self.mng.read_tables(table)
     self.output.delete(1.0, tk.END)
     if isinstance(data, pd.DataFrame):
        self.output.insert(tk.END, '🫵'+data.to_string(index=False))
     else:  
        self.output.insert(tk.END, f"{data}")

    
    def run_update(self):
     table = self.tbentry.get().strip()
     col   = self.centry.get().strip()
     val   = self.vntry.get().strip()
     wcol  = self.c2entry.get().strip()
     chval = self.chventry.get().strip()
     self.output.delete(1.0, tk.END)
     try:
        self.mng.update_Tables(table, col, val, wcol, chval)
        self.output.insert(tk.END, "Updated successfully🫵")
     except Exception as ee:
        self.output.insert(tk.END, f" {ee}")

    def run_insert(self):
     table = self.tbentry.get().strip()
     col   = self.centry.get().strip()
     val   = self.vntry.get().strip()
     self.output.delete(1.0, tk.END)
     try:
        self.mng.insert_tables(table, [col], [val])
        self.output.insert(tk.END, "Inserted successfully🫵")
     except Exception as e:
        self.output.insert(tk.END, f"{e}")

    def run_delete(self):
     table = self.tbentry.get().strip()
     wcol  = self.c2entry.get().strip()
     chval = self.chventry.get().strip()
     self.output.delete(1.0, tk.END)
     try:
        self.mng.delete_Rows(table, wcol, chval)
        self.output.insert(tk.END, "Deleted successfully🫵")
     except Exception as e:
        self.output.insert(tk.END, f"{e}")

    def run_bulk(self):
        table=self.tbentry.get().strip()
        csv=self.bentry.get().strip()
        self.output.delete(1.0,END)
        try:
          self.mng.bulk_insert(table,csv)
          self.output.insert(tk.END,"Insertion Completed🫵")
        except Exception as ee :
           self.output.insert(tk.END,f"{ee}")

    def prepmonth(self):
       df =self.mng.read_tables("Transactions") 
       df["amount_date"]=pd.to_datetime(df["amount_date"]) #<<<< converting string to datetime >>>> pandas fetch data as an string through sql 
       df["month"]=df['amount_date'].dt.strftime("%b")
       w=df.groupby(["month","type"])['Amount'].sum().reset_index()
       x=w.pivot(index='month',columns='type',values='Amount')
       x=x.fillna(0)
       x=x.reset_index()
       self.ch.monthly_income_chart(x)

    def bnktype(self):
       self.ch.acpie_chart(self.mng.read_tables("Accounts"))

    def mnthwise_expense(self):

        df =self.mng.read_tables("Transactions") 
        df["amount_date"]=pd.to_datetime(df["amount_date"]) 
        df["month"]=df['amount_date'].dt.strftime("%b")
        x=df[df["type"] == "Expense"]
        w= x.groupby("month")["Amount"].sum().reset_index()
        self.ch.monthwise_expense(w)

    def top5(self):
       t =self.mng.read_tables("Transactions")
       c = self.mng.read_tables("Categories")
       x =t[t["type"] == "Expense"] # filter only expense >>
       merge = x.merge(c,on="category_id") # join the tables >>
       g = merge.groupby("category_name")["Amount"].sum().reset_index()
       top5 =g.sort_values("Amount").head(5)
       self.ch.top5(top5)


    


       
       
       

       



if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
