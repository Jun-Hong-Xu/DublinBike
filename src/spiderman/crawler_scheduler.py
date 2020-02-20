import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import crawler_insert_table


def timed_task():
    # crawler_insert_table.main()
    f = open("crawler_log.txt", 'a')
    f.write(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-7])
    f.write("\n")
    f.write("Table station has updated with: %i rows. \n" %crawler_insert_table.station_renew_row)
    f.write("Table station_weather has updated with: %i rows. \n" %crawler_insert_table.station_weather_renew_row)
    f.close()


if __name__ == '__main__':
    # Input start time and end time
    start = input("Enter the start time: ")
    end = input("Enter the end time: ")

    # Create the instance of schedulers
    scheduler = BackgroundScheduler()

    # Set the trigger to interval, and interval is 300 second (5 minutes)
    # start_date = "2020-2-19 20:43:20"
    scheduler.add_job(timed_task, 'interval', seconds=1, start_date=start, end_date=end)

    # Start the scheduler
    scheduler.start()
