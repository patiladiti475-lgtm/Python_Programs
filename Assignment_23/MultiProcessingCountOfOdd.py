# ---------------------------------------------------------
# Question:
# Write a Python Program that uses
# multiprocessing.Pool to count how many
# odd numbers exist between 1 and N
# for every number in the given list.
# Display the Process ID, Input Number,
# and Odd Number Count.
# ---------------------------------------------------------

import multiprocessing
import os

def OddCount(no):

    count = 0

    for i in range(1, no + 1, 2):
        count = count + 1

    return (os.getpid(), no, count)

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")
    for i in range(size):
        data.append(int(input()))

    print("List of elements :", data)

    pobj = multiprocessing.Pool()

    Result = pobj.map(OddCount, data)

    pobj.close()
    pobj.join()

    pid = []
    number = []
    oddcount = []

    for p, n, c in Result:
        pid.append(p)
        number.append(n)
        oddcount.append(c)

    print("Process ID       :", pid)
    print("Input Number     :", number)
    print("Odd Number Count :", oddcount)

if __name__ == "__main__":
    main()