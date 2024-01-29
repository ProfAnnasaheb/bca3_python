import calendar

#to disply month calendar
print(calendar.month(2023,10))

#to disply year calendar
print(calendar.calendar(2023))

#to disply weekday count- monday starts with '0'
print(calendar.weekday(2023,10,12))

#check leap year or not
print(calendar.isleap(2008))
print(calendar.isleap(2023))

#check leap year between two years
print(calendar.leapdays(2000,2017))

#help window
print(help(calendar))
