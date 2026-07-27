#python ProcessSurvellience.py 2 Marvell4ousLog
#python ProcessSurvellience.py time_interval Folder_Name
#               0                   1             2
#len(sys.argv)->3
#python ProcessSurvellience.py --h
#python ProcessSurvellience.py --u
import psutil 
import sys
import os
import time

def platformSurvillience(Foldername):
    Border="-"*50
    
    Ret = False
    
    Ret = os.path.exists(Foldername)
    if (Ret == True):
        Ret = os.path.isdir(Foldername)
        if (Ret == False):
            print("Unable to proceesd as directory name is existing but not a Directory")
            return
    else:
        os.mkdir(Foldername)
        print("Directory for the log file gets created successfully")
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    FileName = os.path.join(Foldername,"Marvellous_%s.log " %timestamp)
    Fobj = open(FileName,"w")
    
    print(f"Log file gets successfully gets created with name {FileName}")
    
def main():
    Border="-"*50
    print(Border)
    print("------Marvellous Platfrom Survellience System------")
    print(Border)

    #--h and --u handling
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is use to perform")
            print("1:It fetch information of running processes")
            print("2.It fetch information about primary storage as RAM")
            print("3.It fetch information about secondary storage as HDD")
            print("4.It fetch information about the microprocessor")
            print("5.It gets auto scheduled periodically")
            print("6.It maintains all records into log file")
            print("7.It sends log files through mail periodically")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as:")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval: Time in minutes for periodic execution")
            print("Folder_Name: Name of folder for the log file creation")

        else:
            print("Unable to process as arguments are not matching")
            print("Please use --h or --u flag for getting more details")

    #Actual project code
    elif(len(sys.argv)==3):
        platformSurvillience(sys.argv[2])

    else:
        print("Invalid number of arguments")
        print("Unable to process as argument are not matching")
        print("Please use --h or --u flag for getting more details")




    print(Border)
    print("------Thank You for Using our Automation System------")
    print(Border)
    
if __name__=="__main__":
    main()
