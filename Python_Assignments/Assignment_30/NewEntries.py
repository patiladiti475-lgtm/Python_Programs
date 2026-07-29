#------------------------------------------------------------------
# Question 5
# Schedule a task that executes every 5 minutes.
# Write the current date and time into Marvellous.txt.
# Append new entries without removing previous entries.
#-------------------------------------------------------------------

import schedule
import time
import datetime

def WriteFile():

    FileObj = open("Marvellous.txt", "a")

    Current = datetime.datetime.now()

    FileObj.write("Task executed at: " + Current.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    FileObj.close()

schedule.every(1).minutes.do(WriteFile)

while True:
    schedule.run_pending()
    time.sleep(1)