# ---------------------------------------------------------
# Question:
# Write a program which contains filter(), map() and reduce()
# in it. Filter numbers >=70 and <=90.
# Map function increases each number by 10.
# Reduce function returns product of all numbers.
# ---------------------------------------------------------

from functools import reduce

CheckRange = lambda number : 70 <= number <=90

Increase = lambda number : number + 10

Product = lambda No1,No2 : No1 * No2


def main():

    size = int(input("Enter the no of elements : "))

    data = []
    print("Elements are :")
    for _ in range(size):
        data.append(int(input()))
    
    filtered_data = list(filter(CheckRange,data))

    mapped_data = list(map(Increase,filtered_data))

    result = reduce(Product,mapped_data)

    print("Original List       : ",data)
    print("List after filter   : ",filtered_data)
    print("List after map      : ",mapped_data)
    print("Output of reduce    : ",result)
    
if __name__ == "__main__":
    main()