# ---------------------------------------------------------
# Question:
# Design a Python application that creates two
# threads named EvenList and OddList.
# Both threads accept a list of integers.
# EvenList:
# Display all even elements and their sum.
# OddList:
# Display all odd elements and their sum.
# ---------------------------------------------------------

import threading

def EvenList(data):
    
    sum = 0

    print("Even Elements :", end=" ")

    for number in data:
        if number % 2 == 0:
            print(number, end=" ")
            sum = sum + number

    print("\nSum of Even Elements :", sum)

def OddList(data):
    
    sum = 0

    print("Odd Elements  :", end=" ")

    for number in data:
        if number % 2 != 0:
            print(number, end=" ")
            sum = sum + number

    print("\nSum of Odd Elements :", sum)

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")

    for i in range(size):
        data.append(int(input()))

    even_thread = threading.Thread(target=EvenList,args=(data,),)

    odd_thread = threading.Thread(target=OddList,args=(data,),)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()