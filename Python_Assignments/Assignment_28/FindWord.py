#-----------------------------------------------------------------
# Question 5
# Accept a file name and a word from the user.
# Check whether the word is present in the file.
# Display whether the word is found or not.
#------------------------------------------------------------------

def main():

    FileName = input("Enter File Name : ")
    Word = input("Enter Word to Search : ")

    FileObj = open(FileName, "r")

    Data = FileObj.read()

    if Word in Data:
        print("Word Found")
    else:
        print("Word Not Found")

    FileObj.close()


if __name__ == "__main__":
    main()