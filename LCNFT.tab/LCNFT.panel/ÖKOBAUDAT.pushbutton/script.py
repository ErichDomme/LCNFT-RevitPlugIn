import xml.etree.ElementTree as ET
import requests

# Make the GET request
response = requests.get('https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8/processes')

# Check if the request was successful
if response.status_code == 200 and response.content:
    # Parse the XML response
    root = ET.fromstring(response.content)

    # Now you can iterate over the elements and extract data
    for process in root.findall('{http://www.ilcd-network.org/ILCD/ServiceAPI}process'):
        # Extract UUID, name, classification, etc.
        uuid = process.find('{http://www.ilcd-network.org/ILCD/ServiceAPI}uuid').text
        names = process.findall('{http://www.ilcd-network.org/ILCD/ServiceAPI}name')
        for name in names:
            lang = name.attrib['{http://www.w3.org/XML/1998/namespace}lang']
            value = name.text
            print(f"Name ({lang}): {value}")
        
        # Add additional parsing as needed for your application

else:
    print('Failed to retrieve data:', response.status_code)
