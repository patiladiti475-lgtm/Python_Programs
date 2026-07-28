#-------------------------------------------------------------------------------
# Question 2
# Create a class Circle.
# Instance variables: Radius, Area, Circumference
# Class variable: PI = 3.14
# Constructor initializes all variables to 0.0
# Methods:
#   Accept() - Accept radius
#   CalculateArea() - Calculate area
#   CalculateCircumference() - Calculate circumference
#   Display() - Display Radius, Area, and Circumference
# Create multiple objects and call all methods.
#-------------------------------------------------------------------------------


class Circle:
    
    PI=3.14
    
    def __init__(self):
        self.Radius=0.0
        self.Circumference=0.0
        self.Area=0.0

    def Accept(self,Radius):
        self.Radius=Radius

    def CalculateArea(self):
        self.Area=self.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference=2*self.PI*self.Radius

    def Display(self):
        print("Value of Radius:",self.Radius)
        print("Value of Area:",self.Area)
        print("Value of Circumference:",self.Circumference)

print("Enter Details for object 1")
obj1=Circle()
obj1.Accept(10)
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()
print("\n")

print("Enter Details for object 2")
obj2=Circle()
obj2.Accept(20)
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
print("\n")

print("Enter Details for object 3")
obj3=Circle()
obj3.Accept(30)
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()
print("\n")