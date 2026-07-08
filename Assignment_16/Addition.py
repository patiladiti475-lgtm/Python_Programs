# ---------------------------------------------------------
# Question:
# Write a program which contains one function named
# Add() which accepts two numbers and returns
# addition of those numbers.
# ---------------------------------------------------------


def Add(Num1, Num2):
    
    return Num1 + Num2

def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))

    result = Add(Num1, Num2)

    print("Addition is :", result)

if __name__ == "__main__":
    main()