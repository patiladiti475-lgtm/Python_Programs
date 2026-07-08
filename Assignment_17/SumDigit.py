# ---------------------------------------------------------
# Question:
# Write a program which accepts one number from the
# user and returns the addition of digits in that number.
# ---------------------------------------------------------

def Digits(number):
    
    total = 0

    while number != 0:
        digit = number % 10
        total = total + digit
        number //= 10

    return total

def main():
    number = int(input("Enter a number : "))

    result = Digits(number)

    print("Sum of digits :", result)

if __name__ == "__main__":
    main()