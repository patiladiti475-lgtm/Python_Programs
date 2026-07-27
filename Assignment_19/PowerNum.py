# ---------------------------------------------------------
# Question:
# Write a program which contains one lambda function
# which accepts one parameter and returns
# power of two.
# ---------------------------------------------------------
Power = lambda no : no ** 2

def main():

    number = int(input("Enter a number : "))

    result = Power(number)

    print("Power of two : ",result)
    
if __name__ == "__main__":
    main()