# ---------------------------------------------------------
# Question:
# Write  a Python Program that uses
# multiprocessing.Pool to calculate the
# sum of all odd numbers from 1 to N
# for every number in the given list.
# Display the Process ID, Input Number,
# and Sum of Odd Numbers.
# ---------------------------------------------------------

import multiprocessing
import os

def SumOdd(no):

    Sum = 0

    for i in range(1, no + 1, 2):
        Sum = Sum + i

    return (os.getpid(), no, Sum)

def main():

    data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd, data)

    pobj.close()
    pobj.join()

    for pid, num, total in Result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Sum of Odd Numbers :", total)
        print()

if __name__ == "__main__":
    main()