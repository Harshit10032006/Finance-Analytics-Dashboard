import matplotlib.pyplot as plt 
import pandas as pd

class Chart:
    def __init__(self):
        pass
    
    def monthly_income_chart(self, df): 
        plt.figure(figsize=(10,8))
        plt.bar(df["month"], df["Income"], label="Income")
        plt.bar(df["month"], df["Expense"], bottom=df["Income"], label="Expense")
        plt.xlabel("-----Months-----")
        plt.ylabel("Amount")
        plt.title("🈷️(Monthly) 💰Income vs ❌Expense")
        plt.legend() # explain the colors 
        plt.show()
        
    
    def acpie_chart(self,df):
        count=df["account_type"].value_counts() # counts each unique value  appeared
        plt.figure(figsize=(7,7))
        plt.pie(count.values,
        labels=count.index)
        plt.title("Account Types")
        plt.legend()
        plt.show()

    
    def monthwise_expense(self,df):
        order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        df["month"] = pd.Categorical(df["month"], categories=order)
        df = df.sort_values("month")
        months = df["month"]
        expenses = df["Amount"]
        plt.figure(figsize=(5,5))
        plt.plot(months, expenses, marker="o")
        plt.xlabel("Months")
        plt.ylabel("Total Expense")
        plt.title("Month wise  Expense")
        plt.grid()
        plt.show()

    def top5(self,df):
        names = df["category_name"]
        values=df["Amount"]
        plt.figure(figsize=(5,5))
        plt.pie(values,labels=names)
        plt.legend()
        plt.title("Top 5 Expense Categories")
        plt.show()


