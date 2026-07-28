#--------------------------------------------------------------------
# Question 3
# Accept a file name from the user.
# Display the contents of the file line by line.
#---------------------------------------------------------------------

def main():
    
    FileName = input("Enter File Name : ")

    FileObj = open(FileName, "r")

    for Line in FileObj:
        print(Line, end="")

    FileObj.close()


if __name__ == "__main__":
    main()