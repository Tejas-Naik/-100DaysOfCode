import datetime as dt

# if you wanna get the current time you use dattime class and inside that there is a 'now' method we can use
current_time = dt.datetime.now()
"""
    Now the current_time has a string like '2021-02-10 19:29:30.989673' which is not very useful o get best results 
    we can use:
        current_time.year
        current_time.month
        current_time.day
        current_time.hour
        current_time.minute
        current_time.second
        
        current_time.weekday() # remember this is a method
"""

# creating new datetime objects
date_of_birth = dt.datetime(year=2005, month=9, day=19)
print(date_of_birth)

