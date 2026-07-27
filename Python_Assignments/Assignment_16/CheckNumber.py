# ---------------------------------------------------------
# Question:
# Write a program which accepts one number from the user
# and checks whether that number is positive,
# negative or zero.
# ---------------------------------------------------------


def ChkNum(No):
    
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    num = int(input("Enter a number : "))
    ChkNum(num)


if __name__ == "__main__":
    main()