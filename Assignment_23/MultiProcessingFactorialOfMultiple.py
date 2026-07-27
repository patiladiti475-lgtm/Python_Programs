# ---------------------------------------------------------
# Question:
# Write a Python Program that uses
# multiprocessing.Pool to calculate the
# factorial of multiple numbers simultaneously.
# Display the Process ID, Input Number,
# and Factorial.
# ---------------------------------------------------------

import multiprocessing
import os

def Factorial(no):

    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    return (os.getpid(), no, fact)

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
    number = []
    factorial = []

    for p, n, f in Result:
        pid.append(p)
        number.append(n)
        factorial.append(f)

    print("Process ID  :", pid)
    print("Input Number:", number)
    print("Factorial   :", factorial)

if __name__ == "__main__":
    main()