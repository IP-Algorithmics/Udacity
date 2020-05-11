"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
dictionary = dict()

# O(4n) - since "in" is O(1)
for call in calls:
    # Checks both receiver and caller since it it the same number.
    # The call doesn't have an end timestamp so only the dudration will be added
    if(call[0] in dictionary):
        dictionary[call[0]] += int(call[3])
    else:
        dictionary[call[0]] = int(call[3])

    if(call[1] in dictionary):
        dictionary[call[1]] += int(call[3])
    else:
        dictionary[call[1]] = int(call[3])

# O(n)
longestCall = max(dictionary, key=dictionary.get)

print(
    f'{longestCall} spent the longest time, {dictionary[longestCall]} seconds, on the phone during September 2016.')

# Complexity: O(n)
