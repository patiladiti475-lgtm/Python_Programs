#-----------------------------------------------------------
# Question 1
# Accept a file name from the user.
# Count the total number of lines in the file.
# Display the total number of lines.
#------------------------------------------------------------

def main():
    
    FileName = input("Enter File Name : ")

    FileObj = open(FileName, "r")

    Count = 0

    for Line in FileObj:
        Count = Count + 1

    print("Total number of lines :", Count)

    FileObj.close()


if __name__ == "__main__":
    main()