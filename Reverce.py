def Reverse(no):
    Rev = 0
    
    while no > 0:
        Digit = no % 10
        Rev = Rev * 10 + Digit
        no = no // 10
        
    print("Reverse number is:", Rev)

Num = int(input("Enter a number :"))

Reverse(Num)