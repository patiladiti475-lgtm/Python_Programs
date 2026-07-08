# ---------------------------------------------------------
# Question:
# Design a Python application that creates two
# separate threads named Even and Odd.
# Even thread displays first 10 even numbers.
# Odd thread displays first 10 odd numbers.
# ---------------------------------------------------------

import threading 

def Even():

    print("Even Thread Started")

    for no in range(2,21,2):
        print(no, end =" ")

    print("\nEven Thread Completed")

def Odd():

    print("Odd Thread Started")

    for no in range(1,20,2):
        print(no,end =" ")

    print("\nOdd Thread Completed")

def main():
    
    even_thread = threading.Thread(target = Even, name ="Even")  #name is an optional parameter but recommended

    odd_thread = threading.Thread(target= Odd, name = "Odd")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
