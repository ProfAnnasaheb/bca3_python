import datetime as dt

#print todays date
curdate=dt.date.today()
print(curdate)

#assign custom date
date1=dt.date(2022,11,5)
print(date1)

#current date year+month+day wise
print("year:",curdate.year)
print("month:",curdate.month)
print("day:",curdate.day)

#print currunt datetime and time only
current_datetime = dt.datetime.now()
print("Current datetime is:",current_datetime)
current_time = dt.datetime.now().time()
print("Current time only is:",current_time)

#time object
time1=dt.time(10,50,30,43533)
print(time1)

#print hour min sec and milisec seperatly
print("Hour",time1.hour)
print("Min",time1.minute)
print("Sec",time1.second)
print("Milisec",time1.microsecond)

#diffrence between between two dates
current_datetime = dt.datetime.now()
new_date=dt.datetime(2024,1,1)
rem_dur=new_date-current_datetime
print("Diffrene between two date is:",rem_dur)
