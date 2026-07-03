#Accept:Multiparametr
#Return:one value

def Marvellous(value1, value2):
    print("inside marvellous:",value1,value2)
    return 21,51

def main():
    ret1,ret2=Marvellous(10,20)
    print("Returned value is :",ret1,ret2)
if __name__ == "__main__":
    main()
    