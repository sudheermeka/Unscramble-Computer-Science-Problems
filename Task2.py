"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

time_spent_map = {}
for row in calls:
    format_date = datetime.strptime(row[2].split(" ")[0], '%d-%m-%Y')
    if format_date.month != 9 or format_date.year != 2016:
        continue 
    if row[0] not in time_spent_map:
        time_spent_map[row[0]] = 0
    if row[1] not in time_spent_map:
        time_spent_map[row[1]] = 0
    
    time_spent_map[row[0]] += int(row[3])
    time_spent_map[row[1]] += int(row[3])

number = None
max_time = None
for key, value in time_spent_map.items():
    if number is None or max_time < value:
        number = key
        max_time = value

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, max_time))        
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

