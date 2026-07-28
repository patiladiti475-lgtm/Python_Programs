#-------------------------------------------------------------------------
# Question 3
# Create a class Numbers.
# Instance variable: Value
# Constructor accepts a number and initializes Value.
# Methods:
#   ChkPrime() - Check whether the number is prime
#   ChkPerfect() - Check whether the number is perfect
#   Factors() - Display all factors of the number
#   SumFactors() - Return the sum of all factors
# Create multiple objects and call all methods.
#---------------------------------------------------------------------------

class Numbers:
    
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    
    def ChkPerfect(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i

        return Sum == self.Value

    
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    
    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum += i
        return Sum



Obj1 = Numbers(6)
Obj2 = Numbers(13)

print("Object 1")
print("Prime :", Obj1.ChkPrime())
print("Perfect :", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors :", Obj1.SumFactors())
print("\n")

print("Object 2")
print("Prime :", Obj2.ChkPrime())
print("Perfect :", Obj2.ChkPerfect())
Obj2.Factors()
print("Sum of Factors :", Obj2.SumFactors())