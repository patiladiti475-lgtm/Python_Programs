# ---------------------------------------------------------
# Question:
# Write a program which accepts N numbers from user
# and stores them into a list.
# Return the maximum element.
# ---------------------------------------------------------

def MaxList(data):
    maximum = data[0]
    for number in data:
        if number > maximum:
            maximum = number
    return maximum

def main():
    
    size = int(input("Enter the no of elements : "))

    data = []

    print("Enter the Elements : ")

    for _ in range(size):
        data.append(int(input()))
    
    result = MaxList(data)

    print("Maximum element is : ",result)

if __name__ == "__main__":
    main()