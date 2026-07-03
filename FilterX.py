def CheckEven(no):
    return(no % 2 == 0)

def main():
    Data = [13,12,8,10,11,20]
    print("input data is :", Data)
    FData = list(filter(CheckEven,Data))
    print("data after filter is ", FData)
    
if __name__ == "__main__":
    main()    