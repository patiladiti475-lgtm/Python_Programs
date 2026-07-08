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
    SumEven(1000000)
    Sumodd(10000000)
    
if __name__ == "__main__":
    main()