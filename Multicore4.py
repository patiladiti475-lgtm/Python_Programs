import multiprocessing
import os
import time

def SumCube(no):
    print("process is running with PID : ", os.getpid())
    Sum = 0
    
    for i in range(1, no + 1):
        Sum = Sum + (i ** 3)
        
    return Sum
    
def main():
    data = [100000, 200000, 300000, 400000, 5000000]
    Result = []
    start_time = time.perf_counter()
    
    pobj = multiprocessing.Pool()
    
    Result = pobj.map(SumCube, data)
    
    pobj.close()
    pobj.join()
        
    end_time = time.perf_counter()
    print("Result is: ")
    print(Result)
    
    print(f"Time Required : {end_time-start_time:.4f} seconds")
    
if __name__ == "__main__":
     main()