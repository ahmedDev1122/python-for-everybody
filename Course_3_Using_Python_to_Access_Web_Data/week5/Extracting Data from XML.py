'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2163805.xml (Sum ends with 61)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

import urllib.request
import xml.etree.ElementTree as ET

# Prompt the user for the URL
url = input('Enter location: ')
print('Retrieving', url)

# Read the XML data from the URL
response = urllib.request.urlopen(url)
data = response.read()
print('Retrieved', len(data), 'characters')

# Parse the XML from the retrieved data
tree = ET.fromstring(data)

# Find all <count> elements using XPath
counts = tree.findall('.//count')

# Calculate the total sum of the count values
total = 0
for count in counts:
    total += int(count.text)

# Print the number of count elements and their total sum
print('Count:', len(counts))
print('Sum:', total)
 