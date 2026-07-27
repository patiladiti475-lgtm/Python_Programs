# ---------------------------------------------------------
# Question:
# Design a Python application that creates
# two threads.
# Thread1:
# Display the maximum element from the list.
# Thread2:
# Display the minimum element from the list.
# ---------------------------------------------------------

import threading

def Maximum(data):
    maximum = data[0]

    for number in data:
        if number > maximum:
            maximum = number
    print("Maximum Element :", maximum)

def Minimum(data):
    minimum = data[0]

    for number in data:
        if number < minimum:
            minimum = number
    print("Minimum Element :", minimum)

def main():
    size = int(input("Enter number of elements : "))
    data = []

    print("Enter the elements :")
    for i in range(size):
        data.append(int(input()))

    maximum_thread = threading.Thread(target=Maximum,args=(data,))

    minimum_thread = threading.Thread(target=Minimum,args=(data,))

    maximum_thread.start()
    minimum_thread.start()

    maximum_thread.join()
    minimum_thread.join()

    print("\nExit from main")

if __name__ == "__main__":
    main()