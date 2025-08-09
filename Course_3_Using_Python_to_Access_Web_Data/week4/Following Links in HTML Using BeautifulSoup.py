'''
Following Links in Python

In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
Last name in sequence: Anayah
Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Blanka.html 
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: L
'''

import urllib.request
from bs4 import BeautifulSoup

# Ask for input values
url = input("Enter URL: ")
count = int(input("Enter count: "))      # How many times to follow link
position = int(input("Enter position: "))  # Which link to follow (1-based)

# Repeat the process count times
for i in range(count):
    print("Retrieving:", url)
    
    # Open and read the HTML
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    
    # Find all anchor <a> tags
    links = soup.find_all('a')
    
    # Get the link at the required position (minus 1 because Python is 0-based)
    url = links[position - 1].get('href')

# After the loop ends, the final URL is reached
print("The last URL is:", url)
# Extract the last name from the URL (e.g. known_by_Name.html)
last_name = url.split('_')[-1].split('.')[0]
print("The answer to the assignment is:", last_name)
