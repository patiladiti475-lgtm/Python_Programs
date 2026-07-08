from functools import reduce

Num = [11,22,33,44,55]

Addition = reduce(lambda x,y: x + y, Num)

print("Original list :", Num)
print("Addition of all elements :", Addition)