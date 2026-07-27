# ---------------------------------------------------------
# Question:
# Write a program which contains one lambda function
# which accepts two parameters and returns
# multiplication.
# ---------------------------------------------------------


Multiplication = lambda No1,No2 : No1 * No2

def main():

    first_no = int(input("Enter 1st Number : "))
    second_no = int(input("Enter 2nd Number : "))

    Result = Multiplication(first_no,second_no)

    print("Multiplication is : ",Result)

if __name__ == "__main__":
    main()