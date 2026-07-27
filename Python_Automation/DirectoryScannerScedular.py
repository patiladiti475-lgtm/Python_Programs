import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath = "Marvellous"):
    Border = "_"*40
    timestamp = time.ctime()
    logfileName = "Marvellous%s.log"%(timestamp)
    logfileName = logfileName.replace(",""_")
    logfileName = logfileName.replace(":""_")
    
    print("log file gets created with name is:", logfileName)

    
    fobj = open("marvellous.txt","w")
    fobj.write(Border*"\n")
    fobj.write("Files from thr directory are:")
    fobj.write("Automation script \n")
    for folderName, Subfolder, fileName in os.walk(DirectoryPath):
        for fName in fileName:
            fobj.write(fName"\n")
    fobj.write(Border"\n")
    fobj.write("file gets :", timestamp)
    fobj.write(Border"\n")
    fobj.close()        
def main():
    Border = "_"*40
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) == 2):     # input length
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1]== "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("Directory name should be absolute path")
        else:
            Schedule.every(1).minute.do(DirectoryScanner)
            
            while True:
                Schedule.run_pending()
                time.sleep(1)
            
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)

if __name__ == "__main__":
    main()