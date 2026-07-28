#---------------------------------------------------------------------
# Question 5
# Accept a file name and a string from the user.
# Count the frequency of the string in the file.
# Display the frequency.
#----------------------------------------------------------------------

def main():
    
    FileName = input("Enter File Name : ")
    String = input("Enter String : ")

    FileObj = open(FileName, "r")

    Data = FileObj.read()

    Count = Data.count(String)

    print("Frequency of", String, "is", Count)

    FileObj.close()


if __name__ == "__main__":
    main()