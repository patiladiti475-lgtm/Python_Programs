import time
import os
import multiprocessing

def sumEven(no):
    print(f"PID of Sumeven:{os.getpid()} PPID of Sumeven {os.getppid()}")
    sum=0
    for i in range(2,no,2):
        sum=sum+i
    print("Sum of even:",sum)

def sumodd(no):
    print(f"PID of Sumodd:{os.getpid()} PPID of Sumodd {os.getppid()}")
    sum=0
    for i in range(1,no,2):
        sum=sum+i
    print("Sum of odd",sum)

def main():
    print(f"PID of main:{os.getpid()} PPID of main {os.getppid()}")
    start_time=time.perf_counter()

    tboj1=multiprocessing.Process(target=sumEven,args=(100,))
    tboj2=multiprocessing.Process(target=sumodd,args=(100,))
    tboj1.start()
    tboj2.start()
    tboj1.join()
    tboj2.join()
    end_time=time.perf_counter()
    print(f"Time requires is: {end_time-start_time:4f}")

if __name__=="__main__":
    main()