def CheckPrime(no):
    count = 0

    for i in range(1, no + 1):
        if no % i == 0:
            count = count + 1

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")


num = int(input("Enter a number: "))


CheckPrime(num)