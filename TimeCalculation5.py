import time

def Factorial(no):
    Fact = 1
    
    for i in range(1, no +1):
        Fact = Fact * i
        
    return Fact

def main():
    value = int(input("enter a number :"))
    
    start_time = time.perf_counter()
    
    ret = Factorial(value)
    
    end_time = time.perf_counter()
    
    print(f"Factorial of {value} is {ret}")
    
    print(f"Time required is : {end_time-start_time:.5f} seconds")
    
if __name__ == "__main__":
    main()