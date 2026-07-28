#-----------------------------------------------------------------------
# Question 4
# Accept two file names through command line arguments.
# Compare both files.
# If contents are same, display Success.
# Otherwise, display Failure.
#------------------------------------------------------------------------

def main():
    
    File1 = input("Enter First File Name : ")
    File2 = input("Enter Second File Name : ")

    Obj1 = open(File1, "r")
    Obj2 = open(File2, "r")

    Data1 = Obj1.read()
    Data2 = Obj2.read()

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")

    Obj1.close()
    Obj2.close()

if __name__ == "__main__":
    main()