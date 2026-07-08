# ---------------------------------------------------------
# Question:
# Create one module named Arithmetic which contains
# Add(), Sub(), Mult() and Div().
# Imported Module : ArithmeticX
# ---------------------------------------------------------

import Arithmetic1

def main():

    first_no = int(input("Enter first number : "))
    second_no = int(input("Enter second number : "))

    print("Addition       :", Arithmetic1.Add(first_no, second_no))
    print("Subtraction    :", Arithmetic1.Sub(first_no, second_no))
    print("Multiplication :", Arithmetic1.Mult(first_no, second_no))
    print("Division       :", Arithmetic1.Div(first_no, second_no))

if __name__ == "__main__":
    main()