# ---------------------------------------------------------
# Question:
# Write a Python program that accepts
# a list of integers and uses Pool.map()
#  to calculate
# 1^5 + 2^5 + 3^5 + ... + N^5
# for every element in the list.
# Display the result for each number.
# ---------------------------------------------------------


import multiprocessing
import time

def SumOfPower(no):

    total = 0
    for i in range(1, no + 1):
        total = total + (i ** 5)
    return total

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")
    
    for i in range(size):
        data.append(int(input()))

    print("List of elements :", data)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOfPower, data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Sum of Powers :", Result)

    print(f"Time Required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()