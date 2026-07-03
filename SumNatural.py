def Natural(no):
    sum = 0
    for i in range(1, no + 1):
        sum = sum + i
    print("Sum is:", sum)


num = int(input("Enter a number: "))

Natural(num)