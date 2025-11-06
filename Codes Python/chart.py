import matplotlib.pyplot as plt
# Charts connected to main.py 

class Chart:
    def __init__(self):
        pass
    
    def monthly_income_chart(self, df): # df = Transactions here 
        plt.figure(figsize=(10,8))
        plt.bar(df["month"], df["Income"], label="Income")
        plt.bar(df["month"], df["Expense"], bottom=df["Income"], label="Expense")
        plt.xlabel("Month")
        plt.ylabel("Amount")
        plt.title("🈷️(Monthly) 💰Income vs ❌Expense")
        plt.legend() # explain the colors 
        plt.show()
        
    
    
        




