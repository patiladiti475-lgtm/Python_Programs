CheckEven = lambda no: (no % 2 == 0)

Increment = lambda no : no+1

def main():
    
    Data = [13,12,8,10,11,20]
    print("input data is :", Data)
    
    FData = list(filter(CheckEven,Data))
    print("data after filter is ", FData)
    
    mData = list(map(Increment,FData))
    print("data after map", mData)
    
if __name__ == "__main__":
    main()    