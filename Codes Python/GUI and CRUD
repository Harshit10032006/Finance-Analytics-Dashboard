import pyodbc
import pandas as pd 
import numpy as np 
import tkinter as tk
from tkinter import *

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



class GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600")
        self.root.title("Finance Tracker")
        self.root.config(bg="#0d0086")  
        self.base = manager()

        tk.Label(root,text="Finance Tracker 💲 ",font=("Segoe UI", 22, "bold"),fg="#00adb5",bg="#1e1e1e",pady=9).pack(fill="x")
        input_frame = tk.Frame(root, bg="#111010",bd=20)
        # input_frame.pack(pady=15)
        self.buttonsframe=tk.Frame(root,bg="#111010")
        self.buttonsframe.pack(pady=10)

        tk.Label(input_frame,text=" 📊 Table Name :",font=("Arial", 13,'bold'),fg="#eeeeee",bg="#33319B",bd=20).grid(row=0, column=0, padx=10)
        self.tbentry = tk.Entry(input_frame,width=40, font=("Consolas", 11), bg="#2b2b2b", fg="#00ffcc", insertbackground="white", relief="flat" )
        self.tbentry.grid(row=0, column=1, padx=5)

        self.clum=tk.Entry()

        readbutton = tk.Button(self.buttonsframe,text=" 2->📖Read Table",command=self.read_table,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        readbutton.grid(row=2, column=0, padx=15)

        updatebutton=tk.Button(self.buttonsframe,text="1->🛠️Update Table",command=self.update_table,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        updatebutton.grid(row=1,column=1,padx=15)

        insertbutton=tk.Button(self.buttonsframe,text="3-> ➕Insert Data,",command=self.update_table,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        insertbutton.grid(row=2,column=1)

        deletebutton=tk.Button(self.buttonsframe,text=" 4->♻️Delete rows,",command=self.update_table,font=("Segoe UI", 11, "bold"),bg="#00adb5",fg="#ffffff",activebackground="#e7ffff",activeforeground="black",bd=10,padx=5,pady=5)
        deletebutton.grid(row=2,column=2)

        text_frame = tk.Frame(root, bg="#1e1e1e")
        text_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # table_frame= pending >>>>
        # column_frame=pending >>>>
        # newvalue_frame=pending>>>>


     

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")

        self.output = tk.Text(text_frame,width=125,height=30,bg="#0f0f0f",fg="#00ffcc",insertbackground="white",font=("Consolas", 10),relief="flat")
        self.output.pack(fill="both", expand=True)

        scrollbar.config(command=self.output.yview)

    def read_table(self):
        table = self.tbentry.get()
        data = self.base.read_tables(table)
        self.output.delete(1.0, tk.END)
        
        if type(data)== pd.DataFrame:
            self.output.insert(tk.END, data.to_string(index=False))
        else:
            self.output.insert(tk.END, f" ❌❌❌❌❌❌ERROR ❌❌❌❌❌❌\n{data}")

    def update_table(self):
        # table = self.tbentry.get()
        return
    
    def insert_table(self):
        return
    
    def delete_rows(self):
        return
    
        

        
        



if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

