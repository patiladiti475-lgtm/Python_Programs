#-----------------------------------------------------------
# Question 4
# Create a task that executes every day at 9:00 AM.
# Print "Namskar..."
# Use schedule.every().day.at("09:00").do(...)
#------------------------------------------------------------

import schedule
import time

def Display():
    print("Namskar...")

def main():
    schedule.every().day.at("09:00").do(Display)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
            