from functools import reduce

Num = [10,25,5,18,30]

Min = reduce(lambda x,y: x if x < y else y, Num)

print("original list : ", Num)
print("Minimum Element : ", Min)