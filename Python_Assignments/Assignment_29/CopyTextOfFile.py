#---------------------------------------------------------------------------
# Question 3
# Accept an existing file name through command line arguments.
# Create Demo.txt and copy all contents into ABC.txt.
#----------------------------------------------------------------------------

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