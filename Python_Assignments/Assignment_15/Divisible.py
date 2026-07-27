Num = [10,30,15,9,78,60,75,22]

Display = list(filter(lambda i: i % 3 == 0 and i % 5 == 0, Num))

print("Numbers List:", Num)
print("Numbers Divisible by 3 and 5 :", Display)