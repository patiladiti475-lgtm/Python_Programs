#------------------------------------------------------------------------
# Question 2
# Accept a file name from the user.
# Open the file and display its entire contents on the screen.
#-------------------------------------------------------------------------

def main():
    
    FileName = input("Enter File Name : ")

    FileObj = open(FileName, "r")

    Data = FileObj.read()

    print("Contents of file:")
    print(Data)

    FileObj.close()


if __name__ == "__main__":
    main()