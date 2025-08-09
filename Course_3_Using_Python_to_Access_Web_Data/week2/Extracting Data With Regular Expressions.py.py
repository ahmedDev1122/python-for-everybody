'''
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.
'''

import re

# For Python 3
fname = input('Enter file name: ')

handle = open(fname)

sum = 0
count = 0

for line in handle:
    f = re.findall('[0-9]+', line)

    for num in f:
        count = count + 1
        sum = sum + int(num)

print('There are', count, 'values with a sum =', sum)
