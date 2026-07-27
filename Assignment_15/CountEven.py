Numbers = [10,20,33,45,11,40,100,66,23]

Count = list(filter(lambda i: i % 2 == 0, Numbers))

print("Numbers list: ", Numbers)
print("Count of all even numbers :", len(Count))