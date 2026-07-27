# ---------------------------------------------------------
# Question:
# Write a program which accepts N numbers from user
# and stores them into a list.
# Return addition of all elements from that list.
# ---------------------------------------------------------

def NumList(data):
    
    sum = 0
    for no in data:
        sum = sum + no
    return sum

def main():
    size = int(input("Enter no of elements : "))
    data = []
    print("Enter the elements : ")
    
    for i in range(size):
        value = int(input())
        data.append(value)

    result = NumList(data)

    print("Sum of elements : :",result)

if __name__ == "__main__":
    main()