import time

def SumEven(no):
    Sum = 0 
    
    for i in range(2, no,2):
        Sum = Sum + i
    print("Summetion of even : ", Sum)
    
#2+6+4+8 = 20        
def Sumodd(no):
    Sum = 0 
    
    for i in range(1, no,2):
        Sum = Sum + i
    print("Summetion of Odd : ", Sum)
        
 #1+3+5+7+9= 25   
def main():
    
    start_time = time.perf_counter() 
    
    SumEven(10000000)
    Sumodd(100000000)
    
    end_time = time.perf_counter()
    
    print(f"time reqires is : {end_time-start_time:4f}")
    
if __name__ == "__main__":
    main()