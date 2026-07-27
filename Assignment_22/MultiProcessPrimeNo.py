# ---------------------------------------------------------
# Question:
# Write a Python program that accepts
# a list of integers and uses Pool.map() 
# to count how many prime numbers
# exist between 1 and N for every element
# in the list.
# Display the prime count for each number.
# ---------------------------------------------------------

import multiprocessing

def PrimeCount(no):

    count = 0

    for i in range(2, no + 1):

        prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break

        if prime:
            count = count + 1

    return count

def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")
    for _ in range(size):
        data.append(int(input()))

    print("List of elements :", data)

    pobj = multiprocessing.Pool()

    Result = pobj.map(PrimeCount, data)

    pobj.close()
    pobj.join()

    print("Prime Count :", Result)

if __name__ == "__main__":
    main()