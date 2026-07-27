# ---------------------------------------------------------
# Question:
# Write a program which accepts one number
# and returns addition of its factors.
# I/P : 12          O/P : 16(1+2+3+4+6)
# ---------------------------------------------------------

def Factors(number):
    
    sum = 0
    for value in range(1, number):
        if number % value == 0:
            sum = sum + value

    return sum

def main():
    number = int(input("Enter a number : "))

    result = Factors(number)

    print("Sum of factors :", result)

if __name__ == "__main__":
    main()