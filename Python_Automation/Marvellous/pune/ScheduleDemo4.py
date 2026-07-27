import schedule
import time 
import datetime
def Display():
    print("Jay Ganesh.......", datetime.datetime.now())
    
def main():
    print("Automation script started")
    schedule.every(1).seconds.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    print("end of automation script")
if __name__ == "__main__":
    main()    