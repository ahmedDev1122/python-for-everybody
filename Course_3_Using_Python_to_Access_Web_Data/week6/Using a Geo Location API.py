'''
Calling a JSON API

In this task, you'll write a Python program that asks the user to enter a location, then sends a request to a web service that returns geographic information in JSON format. The program should extract and display the first plus_code (specifically, the global_code) from the response.

The API used here provides a simplified subset of OpenStreetMap data and is available at:

http://py4e-data.dr-chuck.net/opengeo?

There are no API keys required and no rate limits, so you're free to test your code as many times as needed. If you visit the base URL without any parameters, it will respond with "No address...".

To use the API, you need to pass the location as a query parameter named `q`, and make sure it is properly URL-encoded using Python’s `urllib.parse.urlencode()` method. This helps ensure that spaces and special characters in the location are safely included in the URL.

Once the JSON is retrieved and parsed, the program should look for the `plus_code` section and print the value associated with `global_code`.

This assignment is conceptually similar to the example shown in opengeo.py from the course materials, but uses a fixed data source.

'''

import urllib.request
import urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    params = {'q': address}
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'plus_code' not in js:
        print('Failed to retrieve valid data')
        continue

    print('Plus code', js['plus_code']['global_code'])
