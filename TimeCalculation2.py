def Factorial(no):
    Fact = 1
    
    for i in range(1, no +1):
        Fact = Fact * i
    return Fact

def main():
    value = int(input("enter a number :"))
    
    ret = Factorial(value)
    
    print(f"Factorial of {value} is{ret}")
    
    
if __name__ == "__main__":
    main()