def OddNum(no):
    for i in range(1, no+1, 2):
        print(i, end="  ")
        
Number = int(input("Enter a number:"))
OddNum(Number)