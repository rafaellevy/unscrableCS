"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates."""

numbersCalled = set()
prefixCode = re.compile("\(080\)")

for possibleMatch in calls:
  if prefixCode.match(possibleMatch[0]):
      if possibleMatch[1].startswith("(0"):
            # string slicing on possibleMatch[1]
            areaCode = possibleMatch[1][0:possibleMatch[1].find(')')+1]
      elif possibleMatch[1].startswith(('7', '8', '9')):
            areaCode = possibleMatch[1][0:4]
      elif possibleMatch[1].startswith("140"):
            areaCode = "140"
      numbersCalled.add(areaCode)


    
numbersCalledList = list(numbersCalled)
numbersCalledList.sort()


print("The numbers called by people in Bangalore have codes:")
for number in numbersCalledList:
  print(number)

"""Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?
Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
total = 0.0
receiving_bangalore = 0.0

for possibleMatch in calls:
  if prefixCode.match(possibleMatch[0]):
    total += 1
  if prefixCode.match(possibleMatch[0]) and prefixCode.match(possibleMatch[1]) :
    numbersCalled.add(possibleMatch[0])
    receiving_bangalore += 1


result = receiving_bangalore / total * 100


print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."%result)


"""Time complexity is O(nlogn)"""