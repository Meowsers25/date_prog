from datetime import datetime
from dateutil import relativedelta

date_entry1 = input('Enter start date (i.e. 2017, 7, 4)')
year, month, day = map(int, date_entry1.split(','))
date1 = datetime(year, month, day)
print(date1)

date_entry2 = input('Enter end date (i.e. 2017, 7, 4)')
year1, month1, day1 = map(int, date_entry2.split(','))
date2 = datetime(year1, month1, day1)
print(date2)

difference = relativedelta.relativedelta(date2, date1)
print(difference)


