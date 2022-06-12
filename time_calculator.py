#!/usr/bin/env python
# coding: utf-8

# In[13]:


def add_time(start, duration, dayofweek = None):
    
    new_time = ""



#Conversion of Start 12 hour format to 24 hour format
startFormat =start.split(" ")
startTime = startFormat[0].split(":")
startAmPm = startFormat[1]
startHour = int(startTime[0]) 
startMinute = int(startTime[1])

if startAmPm == "PM" :
    startHour = startHour + 12

#Conversion of start hours into minutes
startMinute = startMinute + (60 * startHour)

#Conversion of duration hours into minutes
durationTime = duration.split(":")
durationHour = int(durationTime[0])
durationMinute = int(durationTime[1])
durationMinute = durationMinute + (60 * durationHour)

#Total minutes
minutes = startMinute + durationMinute

#Minute calculation
finalMinutes = minutes % 60
hours = int(minutes / 60)
if len(str(finalMinutes)) == 1:
    new_time = "0" + str(finalMinutes)
elif len(str(finalMinutes)) == 2:
    new_time = str(finalMinutes)

#Days calculation
hour = hours % 24
days = int(hours / 24)

#Hour and AM/PM calculation
finalHour = hour % 12
if int(hour / 12) == 0:
    finalAmpm = 'Am'
    if finalHours == 0:
        finalHours = 12
    else:
        finalAmPm = 'PM'
        if finalHours == 0:
            finalHours = 12
        new_time = str(finalHours) + ':' + new_time + '' + finalAmPm

#Calculation of day of day week
if not dayofweek == None:
    daysofweek =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    pos = 0
    while True:
        if dayofweek.lower() == daysofweek[pos].lower():
            break
        pos = pos + 1
    newDayofweek = daysofweek[((pos + (days % 7)) % 7)]
    new_time = new_time + "," + newDayofweek

#Final output
if days == 1:
    new_time = new_time + " (next day)"
elif days > 1:
    days = str(days)
    new_time = new_time + " (" + days + " days later)"

    
return new_time


# In[ ]:





# In[ ]:




