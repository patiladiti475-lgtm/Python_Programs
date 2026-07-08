# ---------------------------------------------------------
# Question:
# Design a Python application that creates two
# threads named Thread1 and Thread2.
# Thread1:
# Display numbers from 1 to 50.
# Thread2:
# Display numbers from 50 to 1.
# Thread2 should start only after
# Thread1 has completed execution.
# ---------------------------------------------------------

import threading

def DisplayAscending():
    print("Thread1 Started")

    for number in range(1, 51):
        print(number, end=" ")
    print("\nThread1 Completed")

def DisplayDescending():
    print("Thread2 Started")

    for number in range(50, 0, -1):
        print(number, end=" ")
    print("\nThread2 Completed")

def main():
    thread1 = threading.Thread(target=DisplayAscending)

    thread2 = threading.Thread(target=DisplayDescending)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()