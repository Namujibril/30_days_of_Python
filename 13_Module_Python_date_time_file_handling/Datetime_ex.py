# Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print("now =", now)
print("day =", day)
print("month =", month)
print("year =", year) 
print("hour =", hour)
print("minute =", minute)
print("timestamp =", timestamp) 

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
new_format = now.strftime("%m/%d/%Y, %H:%M:%S")
print(new_format)

# Today is 5 December, 2019. Change this time string to time.
time_string = '5 December, 2019'
time_object = datetime.strptime(time_string, '%d %B, %Y')
print(time_object)

# Calculate the time difference between now and new year.
new_year = datetime(year=2025, month=1, day=23, hour=12, minute=41)
time_difference = new_year - now
print("Time difference =", time_difference)

# Calculate the time difference between 1 January 1970 and now.
epoch = datetime(1970, 1, 1)
print(now - epoch)

# Think, what can you use the datetime module for? Examples:

#Time series analysis
#To get a timestamp of any activities in an application
#Adding posts on a blog

'''
Time Series Analysis.
Tracking trends.
Calculating time deltas.
Visualizing data.
Timestamps in Applications.
Adding Posts on a Blog.
Scheduling Tasks.
Creating recurring events.
'''