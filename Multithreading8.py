import time
import threading

def SumEven(no):
    Sum = 0 
    
    for i in range(2, no,2):
        Sum = Sum + i
    print("Summetion of even : ", Sum)
         
def Sumodd(no):
    Sum = 0 
    
    for i in range(1, no,2):
        Sum = Sum + i
    print("Summetion of Odd : ", Sum)
          
def main():
    
    start_time = time.perf_counter() 
    
    t1 = threading.Thread(target=SumEven, args=(10000000,))
    t2 = threading.Thread(target=Sumodd, args=(10000000,))
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.perf_counter()
    
    print(f"time reqires is : {end_time-start_time:4f}")
    
if __name__ == "__main__":
    main()