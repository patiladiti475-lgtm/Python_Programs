from functools import reduce

CheckEven = lambda no: (no % 2 == 0)

def Increment(no):
    return no+1
 
def Addition(no1, no2):
    return no1 + no2
    

def main():
    
    Data = [13,12,8,10,11,20]
    print("input data is :", Data)
    
    FData = list(filter(CheckEven,Data))
    print("data after filter is ", FData)
    
    mData = list(map(Increment,FData))
    print("data after map", mData)
    
    RData = reduce(Addition,mData)
    print("Data after reduce :", RData)
if __name__ == "__main__":
    main()    