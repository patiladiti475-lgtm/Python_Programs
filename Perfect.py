def Perfect(no):
    sum = 0
    
    for i in range(1, no):
        if no % i == 0:
            sum = sum + i
    if sum == no:
        print("Number is perfect ")
    else:
        print("not a perfect number")
        
        
num = int(input("Enter a number :"))
Perfect(num)