# ---------------------------------------------------------
# Question:
# Design a Python application that creates
# two threads.
# Thread1:
# Compute the sum of elements from a list.
# Thread2:
# Compute the product of elements from the same list.
# Return the results to the main thread.
# ---------------------------------------------------------

import threading

sum_result = 0
product_result = 1

def Sum(data):
    global sum_result
    sum = 0

    for number in data:
        sum = sum + number
    sum_result = sum

def Product(data):
    global product_result
    sum = 1

    for number in data:
        sum = sum * number
    product_result = sum

def main():

    size = int(input("Enter number of elements : "))
    data = []

    print("Enter the elements :")
    for _ in range(size):
        data.append(int(input()))

    sum_thread = threading.Thread(target=Sum,args=(data,))

    product_thread = threading.Thread(target=Product,args=(data,))

    sum_thread.start()
    product_thread.start()

    sum_thread.join()
    product_thread.join()

    print("Sum of elements     :", sum_result)
    print("Product of elements :", product_result)

if __name__ == "__main__":
    main()