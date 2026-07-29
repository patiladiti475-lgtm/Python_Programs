#--------------------------------------------------------
# Question 6
# Schedule two tasks:
# 1. Print "Lunch Time!" every day at 1:00 PM.
# 2. Print "Wrap up work" every day at 6:00 PM.
# Use separate functions for both tasks.
#----------------------------------------------------------

import schedule
import time

def Lunch():
    print("Lunch Time!")

def WrapUp():
    print("Wrap up work")

schedule.every().day.at("13:00").do(Lunch)
schedule.every().day.at("18:00").do(WrapUp)

while True:
    schedule.run_pending()
    time.sleep(1)