checkEven = lambda no: (no % 2 == 0)

      
def main():
    value = int(input("enter number : "))
    
    ret = checkeven(value)     # ret = (value % 2 == 0) 
    
    if(ret == True):
        print("its even number")
    else:
        print("its odd number")
    
        
if __name__ == "__main__":
    main()    