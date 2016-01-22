#!/usr/bin/python

import sys
import datetime

class Hiker:

    def weekday_count_thirteen_every_month(self, start_year):

        weekdays_count = { '0': 0, '1': 0, '2': 0, '3': 0,'4': 0,'5': 0, '6': 0 }
        weekdays = { '0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday','4': 'Friday','5': 'Saturday', '6': 'Sunday' }
        
        current_year = datetime.date.today().year

        for year in range(int(start_year),current_year):
            for month in range(1,13):
    
                date = datetime.date(year, month, 13)
                weekday_number = date.strftime('%w')
                weekdays_count[weekday_number] += 1 

        return weekdays_count

        for i in sorted(weekdays_count):
            print("%s %s" % (weekdays_count[i], weekdays[i]))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Argument count wrong, please provide start year")
        sys.exit(1)

    start_year = sys.argv[1]

    if not start_year.isnumeric():
        print("Please provide a valid year")
        sys.exit(1)

    h = Hiker()
    weekdays_count = h.weekday_count_thirteen_every_month(start_year)
    for i in sorted(weekdays_count):
        print("%s %s" % (weekdays_count[i], weekdays[i]))
