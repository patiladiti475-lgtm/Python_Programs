def SumDigit(no):
    Count = 0
    while no > 0:
        Digit = no % 10
        Count = Count + Digit
        no = no // 10
    print("sum of digit is", Count)
    
Num = int(input("Enter a Number :"))
SumDigit(Num)
    