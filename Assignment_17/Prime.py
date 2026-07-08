# ---------------------------------------------------------
# Question:
# Write a program which accepts one number
# and checks whether it is prime or not.
# I/P : 5        O/P : It is a prime
# ---------------------------------------------------------
def Prime(number):
    
    if number <= 1:
        return False

    for value in range(2, number):
        if number % value == 0:
            return False

    return True

def main():
    number = int(input("Enter a number : "))

    result = Prime(number)

    if result:
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()