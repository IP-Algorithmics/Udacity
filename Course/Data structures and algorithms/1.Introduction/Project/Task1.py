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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def addToSet(set: set, list: list):
    # O(n)
    set.update(list)


def getColumn(list: list, col: int):
    # O(n)
    return [row[col] for row in list]


distinctPhoneNumbers = set()

# O(2n) x 4
addToSet(distinctPhoneNumbers, getColumn(calls, 0))
addToSet(distinctPhoneNumbers, getColumn(calls, 1))
addToSet(distinctPhoneNumbers, getColumn(texts, 0))
addToSet(distinctPhoneNumbers, getColumn(texts, 1))
print(
    f'There are {len(distinctPhoneNumbers)} different telephone numbers in the records.')
# Time complexity: O(n)
