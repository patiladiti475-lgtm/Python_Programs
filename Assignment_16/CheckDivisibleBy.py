# ---------------------------------------------------------
# Question:
# Write a program which contains one function that
# accepts one number from the user and returns
# True if the number is divisible by 5,
# otherwise returns False.
# ---------------------------------------------------------

def Check(number):
    return number % 5 == 0

def main():
    number = int(input("Enter a number : "))

    result = Check(number)

    print(result)

if __name__ == "__main__":
    main()