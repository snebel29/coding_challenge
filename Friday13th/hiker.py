#!/usr/bin/python

import datetime

class Hiker:

    def weekday_of(self, date):
        return date.strftime('%A')

if __name__ == '__main__':

    a = Hiker()

    weekdays_count = { '0': 0, '1': 0, '2': 0, '3': 0,'4': 0,'5': 0, '6': 0 }
    weekdays = { '0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday','4': 'Friday','5': 'Saturday', '6': 'Sunday' }

    for year in range(1905,2016):
        for month in range(1,13):

            date = datetime.date(year, month, 13)
            weekday_number = date.strftime('%w')
            weekdays_count[weekday_number] += 1 
            #print(date.strftime('%Y-%m-%d: %A'))

    for i in sorted(weekdays_count):
        print("%s %s" % (weekdays_count[i], weekdays[i]))
