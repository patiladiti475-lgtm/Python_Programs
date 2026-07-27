import multiprocessing
import os

def SumEven(no):

    Sum = 0

    for i in range(2, no + 1, 2):
        Sum = Sum + i

    return (os.getpid(), no, Sum)

def main():

    data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven, data)

    pobj.close()
    pobj.join()

    for pid, num, total in Result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Sum of Even Numbers :", total)
        print()

if __name__ == "__main__":
    main()