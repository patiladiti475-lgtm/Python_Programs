# ---------------------------------------------------------
# Question:
# Write a program which accepts N numbers from user
# and stores them into a list.
# Return the minimum element.
# ---------------------------------------------------------

def MinList(data):
    minimum = data[0]
    for number in data:
        if number < minimum:
            minimum = number
    return minimum

def main():
    
    size = int(input("Enter the no of elements : "))

    data = []

    print("Enter the Elements : ")

    for _ in range(size):
        data.append(int(input()))
    
    result = MinList(data)

    print("Minimum element is : ",result)

if __name__ == "__main__":
    main()