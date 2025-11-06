import matplotlib.pyplot as plt 


class Chart:
    def __init__(self):
        pass
    
    def monthly_income_chart(self, df): # df = Transactions here 
        plt.figure(figsize=(10,8))
        plt.bar(df["month"], df["Income"], label="Income")
        plt.bar(df["month"], df["Expense"], bottom=df["Income"], label="Expense")
        plt.xlabel("-----Months-----")
        plt.ylabel("Amount")
        plt.title("🈷️(Monthly) 💰Income vs ❌Expense")
        plt.legend() # explain the colors 
        plt.show()
        
    
    def acpie_chart(self,df):# df = Accounts Here
        count=df["account_type"].value_counts() # counts each unique value  appeared
        plt.figure(figsize=(7,7))
        plt.pie(count.values,
        labels=count.index)
        plt.title("Account Types")
        plt.legend()
        plt.show()

    
    def monthwise_expense(self,df):
        months = df["month"]
        expenses = df["Amount"]
        plt.figure(figsize=(5,5))
        plt.plot(months, expenses, marker="o")
        plt.xlabel("Months")
        plt.ylabel("Total Expense")
        plt.title("Month wise  Expense")
        plt.grid()
        plt.show()
        




