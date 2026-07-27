def checkeven(no):
    if(no % 2 == 0):
        print("its even number")
    else:
        print("its odd number")
        
def main():
    value = int(input("enter number : "))
    
    checkeven(value)
        
if __name__ == "__main__":
    main()    