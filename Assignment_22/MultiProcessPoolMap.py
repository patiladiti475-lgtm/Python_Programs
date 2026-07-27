# ---------------------------------------------------------
# Question:
# Write a Python Program that accepts
# a list of integers and uses Pool.map()
# to calculate the sum of squares
# from 1 to N for every element in the list.
# Return the results to the main process.
# ---------------------------------------------------------

import multiprocessing

def SumOfSquares(no):

    total = 0

    for i in range(1, no + 1):
        total = total + (i * i)

    return total

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")
    for i in range(size):
        data.append(int(input()))

    print("List of elements :", data)

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOfSquares, data)

    pobj.close()
    pobj.join()

    print("Sum of Squares :", Result)

if __name__ == "__main__":
    main()