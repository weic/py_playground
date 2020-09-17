#! python3
# ----------------------------------------------------------------
# Count days between 2 random date
# ----------------------------------------------------------------

import datetime
from dateutil import rrule

class CountDaysBetween:
    def __init__(self, start_date, end_date):
        self.start_date = datetime.datetime.strptime(start_date, '%Y, %m, %d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y, %m, %d')
    
    def days(self):
        d = self.end_date - self.start_date
        return d.days if d.days > 0 else False
    
    def weeks(self):
        weeks = rrule.rrule(rrule.WEEKLY, dtstart=self.start_date, until=self.end_date)
        return weeks.count()

f = CountDaysBetween('2020, 3, 18', '2020, 9, 16')
d = f.days()
w = f.weeks()
print(d)
print(w)




