#----------------------------------------------------------------------------------
# Question 4
# Accept two file names from the user.
# First file is an existing file.
# Second file is a new file.
# Copy all contents from the first file to the second file.
#------------------------------------------------------------------------------------

def main():
    
    SourceFile = input("Enter Source File Name : ")
    DestinationFile = input("Enter Destination File Name : ")

    SourceObj = open(SourceFile, "r")
    DestinationObj = open(DestinationFile, "w")

    for Line in SourceObj:
        DestinationObj.write(Line)

    SourceObj.close()
    DestinationObj.close()

    print("Contents copied successfully.")


if __name__ == "__main__":
    main()