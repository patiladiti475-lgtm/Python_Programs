# ---------------------------------------------------------
# Question:
# Write a program which accepts N numbers from user
# and stores them into a list.
# Accept one another number and return
# frequency of that number.
# ---------------------------------------------------------

def Frequency(data, search_element):
    count = 0
    for number in data:
        if number == search_element:
            count = count + 1
    return count

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements :")

    for _ in range(size):
        data.append(int(input()))

    search_element = int(input("Enter element to search : "))

    result = Frequency(data, search_element)

    print("Frequency :", result)

if __name__ == "__main__":
    main()