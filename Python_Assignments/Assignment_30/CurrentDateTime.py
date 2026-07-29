#--------------------------------------------------------------
# Question 2
# Display the current date and time every 1 minute.
# Use the datetime and schedule modules.
#--------------------------------------------------------------

import schedule
import time
import datetime

def Display():
    Current = datetime.datetime.now()
    print("Current Date and Time :", Current.strftime("%d-%m-%Y %I:%M:%S %p"))
    
    
def main():
    
    schedule.every(1).minutes.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == '__main__':
    main()
        
    