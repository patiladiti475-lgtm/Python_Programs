# ---------------------------------------------------------
# Question:
# Write a program which accepts one number
# and prints that number of '*' on the screen.
# ---------------------------------------------------------

def Display(No):
    
    for i in range(No):
        print("*", end=" ")

def main():
    number = int(input("Enter a number : "))
    Display(number)

if __name__ == "__main__":
    main()