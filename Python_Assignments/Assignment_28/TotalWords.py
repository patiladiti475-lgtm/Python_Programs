#-------------------------------------------------------------
# Question 2
# Accept a file name from the user.
# Count the total number of words in the file.
# Display the total number of words.
#--------------------------------------------------------------

def main():
    
    FileName = input("Enter File Name : ")

    FileObj = open(FileName, "r")

    Count = 0

    for Line in FileObj:
        Words = Line.split()
        Count = Count + len(Words)

    print("Total number of words :", Count)

    FileObj.close()


if __name__ == "__main__":
    main()