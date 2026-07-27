import psutil 
import sys
import os
import time
import schedule

def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"]= proc.cpu_percent(None)
        info["memory_percent"]= proc.memory_percent()
        
        listprocess.append(info)
    return listprocess

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
    
    Fobj.write(Border+"\n")
    Fobj.write("------Marvellous Platfrom Survellience System------\n")
    Fobj.write("log file gets created at :"+timestamp+"\n")
    Fobj.write(Border+"\n\n")
    
    Fobj.write("-----------System report-----------------------\n")
    
    #CPU Information
    Fobj.write("numberof active cpu cores :%s\n" %psutil.cpu_count())
    Fobj.write("CPU usage :%s %%\n" %psutil.cpu_percent())
    Fobj.write(Border+"\n")
    
    #RAM Information
    memory = psutil.virtual_memory()
    
    Fobj.write("RAM usage :%s %%\n" %memory.percent)
    Fobj.write("Total RAM Available :%s %%\n" %memory.total)
    
    Fobj.write(Border+"\n")
    
    #Network Usage
    Netobj = psutil.net_io_counters()
    
    Fobj.write("Network usage Report\n")
    Fobj.write("sent : %.2f MB\n" %(Netobj.bytes_sent / (1024 * 1024)))
    Fobj.write("receive : %.2f MB\n" %(Netobj.bytes_recv / (1024 * 1024)))
    
    #Process Log 
    Data = ProcessScan()
    
    for info in Data:
        Fobj.write("PID : %s\n" %info.get("pid"))
        Fobj.write("name : %s\n" %info.get("pid"))
        Fobj.write("Username: %s\n" %info.get("pid"))
        Fobj.write("Status : %s\n" %info.get("pid"))
        Fobj.write("CPU usage :%.2f\n" %info.get("cpu_percent"))
        Fobj.write("RAM usage :%.2f\n" %info.get("memory_percent"))
        #Fobj.write(f"{info}\n")
        Fobj.write(Border+"\n")
    
    Fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    Fobj.write(Border+"\n")
    Fobj.write("-----------End of log file----------------------\n")
    Fobj.write(Border+"\n")
    
    Fobj.close()
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
        #print("CPU Usage :", psutil.cpu_percent())
        print("schedular started successfully")
        print("press ctrl +c to abort the autometion script")
        
        schedule.every(int(sys.argv[1])).minute.do(platformSurvillience, sys.argv[2])
        
        while True:
            schedule.run_pending()
            time.sleep(1)
        
        #platformSurvillience(sys.argv[2])
          

    else:
        print("Invalid number of arguments")
        print("Unable to process as argument are not matching")
        print("Please use --h or --u flag for getting more details")




    print(Border)
    print("------Thank You for Using our Automation System------")
    print(Border)
    
if __name__=="__main__":
    main()
