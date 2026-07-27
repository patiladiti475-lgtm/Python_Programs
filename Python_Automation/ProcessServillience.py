#python processservillience.py 2 marvellouslog
#python ProcessServillience.py Time_interval Folder_name
#         0          1             2
# if (sys.argv) = 3
import psutil
import sys
import os


def main():
    Border = "-"*50
    print(Border)
    print("------Marvellous Platform Servillience system----------")
    print(Border)
    #--h & --u Handling
    if (len(sys.argv)==2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this autometion script is used to perform")
            print("1 : it fetch the information process of running process ")
            print("2 : it it fetch the information about the primary storage as RAM")
            print("3 : it fetch the information about secondary storage as HDD")
            print("4 : it fetvch the information about the Microprocessor")
            print("5 : it gets Autoscheduled periodically")
            print("6 : it maintaians all records into log files")
            print("7 : it sends the log files internally through mails periodically")
            
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("use the automation script as")
        print(f"python {sys.argv[0]} Time interval Folder_name")
           else:
        print("Unable to proceed as arguments are not matching")
        print("please use --h & --u flag for getting more details")
        
    elif       
    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("please use --h & --u flag for getting more details")
    
    print(Border)
    print("------Thankyou for using Our Automation System system----------")
    print(Border)
    
    
    
if __name__ == '__main__':
    main()