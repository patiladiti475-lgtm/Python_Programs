#--------------------------------------------------------------------------------------
# Question 2
# Create a class BankAccount.
# Instance variables: Name, Amount
# Class variable: ROI = 10.5
# Constructor accepts Name and Amount.
# Methods:
#   Display() - Display account holder name and balance
#   Deposit() - Deposit amount into account
#   Withdraw() - Withdraw amount if sufficient balance is available
#   CalculateInterest() - Calculate interest using:
#                         Interest = (Amount * ROI) / 100
# Create multiple objects and call all methods.
#----------------------------------------------------------------------------------------

class BankAccount:
    
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    
    def Display(self):
        print("Name :", self.Name)
        print("Balance :", self.Amount)

    
    def Deposit(self):
        money = float(input("Enter Deposit Amount : "))
        self.Amount += money

    
    def Withdraw(self):
        money = float(input("Enter Withdraw Amount : "))
        if money <= self.Amount:
            self.Amount -= money
        else:
            print("Insufficient Balance")

    
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest



Obj1 = BankAccount("Aditi", 10000)
Obj2 = BankAccount("Prathamesh", 20000)

print("Object 1")
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest :", Obj1.CalculateInterest())
Obj1.Display()

print()

print("Object 2")
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest :", Obj2.CalculateInterest())
Obj2.Display()