from functools import reduce

Numbers = [1,2,3,4,5]

Product = reduce(lambda x,y: x * y, Numbers)

print("Numbers List :", Numbers)
print("Product of all elements :", Product)