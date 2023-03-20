#trying weekdays
#https://pynative.com/python-get-the-day-of-week/#:~:text=We%20can%20use%20the%20weekday,%2C%2002)%20is%20a%20Monday.


#today = datetime.date(2023, 3, 20)
#no = x_date.weekday()

#if no < 5:
 #   print("Date is Weekday")
#else:  # 5 Sat, 6 Sun
 #   print("Date is Weekend")

import datetime

today = datetime.date(2023, 3, 20)
day_of_week = today.weekday()

if day_of_week < 5:
    print("Today is a weekday")
else:  # 5 is Saturday, 6 is Sunday
    print("Todat is a weekend")