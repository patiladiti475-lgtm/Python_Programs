import time
import threading

def SumEven(no):
    
    print("tid of Sumeven thread is : ", threading.get_ident)
         
def Sumodd(no):
    
    print("tid of Sumodd thread is : ", threading.get_ident)
          
def main():
    print("tid of main thread is : ", threading.get_ident)
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