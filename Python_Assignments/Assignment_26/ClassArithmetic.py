#------------------------------------------------------------------------------------
# Question 3
# Create a class Arithmetic.
# Instance variables: Value1, Value2
# Constructor initializes both variables to 0
# Methods:
#   Accept() - Accept Value1 and Value2
#   Addition() - Return addition of Value1 and Value2
#   Subtraction() - Return subtraction of Value1 and Value2
#   Multiplication() - Return multiplication of Value1 and Value2
#   Division() - Return division of Value1 and Value2 (handle division by zero)
# Create multiple objects and call all methods.
#--------------------------------------------------------------------------------------

class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter Value1:"))
        self.Value2=int(input("Enter Value2:"))

    def Addition(self):
        print("Addition is:",self.Value1+self.Value2)

    def Subtraction(self):
            print("Subtraction is:",self.Value1-self.Value2)

    def Multiplication(self):
            print("Multiplication is:",self.Value1*self.Value2)

    def Division(self):
            print("Division is:",self.Value1/self.Value2)

obj1=Arithmetic()
obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()