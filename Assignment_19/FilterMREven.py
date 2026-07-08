# ---------------------------------------------------------
# Question:
# Write a program which contains filter(), map()
# and reduce().
# Filter:
# Keep only even numbers.
# Map:
# Calculate the square of each number.
# Reduce:
# Return the addition of all squared numbers.
# ---------------------------------------------------------

from functools import reduce

CheckEven = lambda number : number % 2 == 0

SquareNo = lambda number : number ** 2

AddSqNo = lambda No1,No2 : No1 + No2

def main():

    size = int(input("Enter the no of elements : "))

    data = []
    print("Elements are :")
    for _ in range(size):
        data.append(int(input()))
    
    filtered_data = list(filter(CheckEven,data))

    mapped_data = list(map(SquareNo,filtered_data))

    result = reduce(AddSqNo,mapped_data)

    print("Original List       : ",data)
    print("List after filter   : ",filtered_data)
    print("List after map      : ",mapped_data)
    print("Output of reduce    : ",result)
    
if __name__ == "__main__":
    main()