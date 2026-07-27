# ---------------------------------------------------------
# Question:
# Design a Python application that creates two
# threads named EvenFactor and OddFactor.
# EvenFactor :
# Display all even factors and their sum.
# OddFactor :
# Display all odd factors and their sum.
# ---------------------------------------------------------

import threading

def EvenFactor(no):
    sum = 0
    print("Even Factors : ",end = " ")

    for value in range(1,no + 1):
        if no % value == 0 and value % 2 == 0:
            print(value, end=" ")
            sum = sum + value
    print("\nSum of Even Factors : ",sum)

def OddFactor(no):
    sum = 0
    print("Odd Factors : ",end = " ")

    for value in range(1,no+1):
        if no % value == 0 and value % 2 != 0:
            print(value,end=" ")
            sum = sum + value
    print("\nSum of Odd Factors :",sum)

def main():
    number = int(input("Enter a number : "))

    even_thread = threading.Thread(target = EvenFactor,args=(number,),name = "EvenFactor")

    odd_thread = threading.Thread(target = OddFactor,args=(number,),name="OddFactor")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()