# This program outputs whether or not today is a weekday.
# Author: Jonathon Grealish
# References:
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://www.w3schools.com/python/python_datetime.asp
# https://stackoverflow.com/questions/46744919/if-else-statement-does-not-give-desired-output

# import date, time and datetime modules to manipulate dates and times
from datetime import date
from datetime import time
from datetime import datetime
import calendar

# establishing a variable today to retrieve today's date.
today = date.today()
# establishing a variable today_day to retrieve the days of the week from the calendar module.
today_day = calendar.day_name[today.weekday()]

# If and Else statements will determine if the current day is a weekday or not.
# today.strftime will format the string of today's date to appear visually clear. 
if today_day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
    print("Yes unfortunately,", today.strftime("%A %B %d %Y,"), "is a weekday.")
else:
    print(today.strftime("%A %B %d %Y,"),"it's the weekend, yay!")