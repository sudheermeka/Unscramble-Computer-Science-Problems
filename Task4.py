"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
marketing_numbers = set()
non_marketing_numbers = set()

for row in texts:
    non_marketing_numbers.add(row[0])
    non_marketing_numbers.add(row[1])
for row in calls:
    non_marketing_numbers.add(row[1])
    marketing_numbers.add(row[0])

    
marketing_numbers -= marketing_numbers & non_marketing_numbers
marketing_numbers = sorted(marketing_numbers)
print("These numbers could be telemarketers: ")
print('\n'.join(marketing_numbers)) 
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

