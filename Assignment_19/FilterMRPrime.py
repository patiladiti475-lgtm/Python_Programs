# ---------------------------------------------------------
# Question:
# Write a program which contains filter(), map()
# and reduce().
# Filter:
# Keep only prime numbers.
# Map:
# Multiply each prime number by 2.
# Reduce:
# Return the maximum number.
# ---------------------------------------------------------

from functools import reduce

def Prime(no):
    if no <= 1:
        return False
    
    for value in range(2,no):
        if no % value == 0:
            return False
    
    return True

Multiply = lambda no : no * 2

Maximum = lambda No1,No2: No1 if No1 > No2 else No2

def main():

    data = []

    size = int(input("Enter the no of elements : "))

    print("Enter the elements :")
    for i in range(size):
        data.append(int(input()))
    
    filtered_data = list(filter(Prime, data))

    mapped_data = list(map(Multiply,filtered_data))

    result = reduce(Maximum, mapped_data)

    print("Original List      :", data)
    print("List after filter  :", filtered_data)
    print("List after map     :", mapped_data)
    print("Output of reduce   :", result)

if __name__ == "__main__":
    main()