'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2163806.json (Sum ends with 55)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

'''

import urllib.request
import json

# Prompt the user for the URL
url = input('Enter location: ')
print('Retrieving', url)

# Read the JSON data from the URL
response = urllib.request.urlopen(url)
data = response.read().decode()
print('Retrieved', len(data), 'characters')

# Parse the JSON data
info = json.loads(data)

# Extract the list of comments
comments = info['comments']

# Calculate the total sum of all 'count' values
total = 0
for item in comments:
    total += item['count']

# Print the number of items and the sum
print('Count:', len(comments))
print('Sum:', total)
