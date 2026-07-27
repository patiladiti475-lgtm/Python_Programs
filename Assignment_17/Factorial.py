# ---------------------------------------------------------
# Question:
# Write a program which accepts one number
# and returns its factorial.
# I/P : 5           O/P : 120
# ---------------------------------------------------------

def Factorial(number):
    fact = 1

    for value in range(1, number + 1):
        fact = fact * value

    return fact

def main():
    number = int(input("Enter a number : "))

    result = Factorial(number)

    print("Factorial :", result)

if __name__ == "__main__":
    main()