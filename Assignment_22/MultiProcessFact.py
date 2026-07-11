# ---------------------------------------------------------
# Question:
# Write a Python program that calculates
# the factorial of multiple numbers
# simultaneously using Pool.map()
# Display:
# 1. Process ID
# 2. Input Number
# 3. Factorial
# ---------------------------------------------------------

import multiprocessing
import os

def Factorial(no):

    fact = 1
    for i in range(1, no + 1):
        fact = fact * i

    return (os.getpid(), fact)

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")
    for i in range(size):
        data.append(int(input()))

    print("List of elements :", data)

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, data)

    pobj.close()
    pobj.join()

    pid = []
    factorial = []

    for p, f in Result:
        pid.append(p)
        factorial.append(f)

    print("Process ID   :", pid)
    print("Input Number :", data)
    print("Factorial    :", factorial)

if __name__ == "__main__":
    main()