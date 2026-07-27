# ---------------------------------------------------------
# Question:
# Design a Python application where multiple threads
# update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter
# multiple times.
# Display the final value of the counter after all
# threads complete execution.
# ---------------------------------------------------------

import threading

counter = 0
lock = threading.Lock()

def Increment():

    global counter
    for i in range(100000):
        lock.acquire()
        counter = counter + 1
        lock.release()

def main():

    thread1 = threading.Thread(target=Increment)

    thread2 = threading.Thread(target=Increment)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Final Counter Value :", counter)

if __name__ == "__main__":
    main()