# ---------------------------------------------------------
# Question:
# Write a program which accepts one number from the
# user and returns the number of digits in that number.
# ---------------------------------------------------------

def Digits(Num):
    
    count = 0

    while Num != 0:
        count = count + 1
        Num //= 10

    return count

def main():
    Number = int(input("Enter a number : "))

    result = Digits(Number)

    print("Number of digits :", result)

if __name__ == "__main__":
    main()