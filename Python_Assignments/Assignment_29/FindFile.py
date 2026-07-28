#----------------------------------------------------------------------------
# Question 1
# Accept a file name from the user.
# Check whether the file exists in the current directory.
# Display whether the file exists or not.
#------------------------------------------------------------------------------

import os

def main():

    FileName = input("Enter File Name : ")

    if os.path.exists(FileName):
        print("File exists")
    else:
        print("File does not exist")


if __name__ == "__main__":
    main()