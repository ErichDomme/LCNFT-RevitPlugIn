import xml.etree.ElementTree as ET
import clr
clr.AddReference('System.Net')
from System.Net import WebClient

# Use WebClient to download the data
client = WebClient()

try:
    # Download the data as a string
    data = client.DownloadString('https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8/processes')
    
    # Parse the XML response
    root = ET.fromstring(data)

    # Now you can iterate over the elements and extract data
    for process in root.findall('{http://www.ilcd-network.org/ILCD/ServiceAPI}process'):
        # Extract UUID, name, classification, etc.
        uuid = process.find('{http://www.ilcd-network.org/ILCD/ServiceAPI}uuid').text
        names = process.findall('{http://www.ilcd-network.org/ILCD/ServiceAPI}name')
        for name in names:
            lang = name.attrib['{http://www.w3.org/XML/1998/namespace}lang']
            value = name.text
            print("Name ({0}): {1}".format(lang, value))
        
        # Add additional parsing as needed for your application

except Exception as e:
    print("Failed to fetch materials: {0}".format(str(e)))
