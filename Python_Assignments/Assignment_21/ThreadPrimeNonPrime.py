# ---------------------------------------------------------
# Question:
# Design a Python application that creates two
# threads named Prime and NonPrime.
# Both threads accept a list of integers.
# Prime:
# Display all prime numbers from the list.
# NonPrime:
# Display all non-prime numbers from the list.
# ---------------------------------------------------------

import threading

def CheckPrime(number):
    if number <= 1:
        return False

    for value in range(2, number):
        if number % value == 0:
            return False
    return True

def Prime(data):
    print("Prime Numbers :", end=" ")

    for number in data:
        if CheckPrime(number):
            print(number, end=" ")
    print()

def NonPrime(data):
    print("Non-Prime Numbers :", end=" ")

    for number in data:
        if not CheckPrime(number):
            print(number, end=" ")
    print()

def main():
    size = int(input("Enter number of elements : "))
    data = []

    print("Enter the elements :")
    for _ in range(size):
        data.append(int(input()))

    prime_thread = threading.Thread(target=Prime,args=(data,))

    non_prime_thread = threading.Thread(target=NonPrime,args=(data,))

    prime_thread.start()
    non_prime_thread.start()

    prime_thread.join()
    non_prime_thread.join()

    print("\nExit from main")

if __name__ == "__main__":
    main()