#-------------------------------------------------------------------
# Question 7
# Perform a file backup every hour.
# Accept source file path and destination directory path.
# Copy the file to the destination.
# Add current date and time to the backup filename.
# Write backup details in backup_log.txt.
# Use shutil module.
#-------------------------------------------------------------------

import schedule
import time
import shutil
import os
import datetime

SourceFile = input("Enter Source File Path : ")
DestinationPath = input("Enter Destination Directory : ")

def Backup():

    Current = datetime.datetime.now()

    FileName = os.path.basename(SourceFile)
    Name, Ext = os.path.splitext(FileName)

    NewFileName = Name + "_" + Current.strftime("%d_%m_%Y_%H_%M_%S") + Ext

    DestinationFile = os.path.join(DestinationPath, NewFileName)

    shutil.copy(SourceFile, DestinationFile)

    LogFile = open("backup_log.txt", "a")
    LogFile.write("Backup completed successfully at " +
                  Current.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    LogFile.close()

    print("Backup Completed")

schedule.every().second.do(Backup)

while True:
    schedule.run_pending()
    time.sleep(1)
