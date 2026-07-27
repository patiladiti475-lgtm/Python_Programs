# ---------------------------------------------------------
# Question:
# Write a program which contains one function named
# ChkNum() which accepts one parameter as number.
# If number is even then display "Even Number"
# otherwise display "Odd Number".
# ---------------------------------------------------------

def ChkNum(number):
    
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    number = int(input("Enter a number : "))

    ChkNum(number)

if __name__ == "__main__":
    main()