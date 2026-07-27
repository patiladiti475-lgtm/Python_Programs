def Summention(Data):
    sum = 0
    
    for no in Data:
        sum = sum + no
    return sum
def main():
    marks = [78,90,56,98,77]
    
    Ret = Summention(marks)
        
    print("Addition is :", Ret)    
    
if __name__ == "__main__":
    main()
