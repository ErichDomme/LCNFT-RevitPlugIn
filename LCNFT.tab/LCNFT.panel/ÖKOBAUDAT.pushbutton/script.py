import xml.etree.ElementTree as ET
import clr
clr.AddReference('System.Net')
from System.Net import WebClient

# Use WebClient to download the data
client = WebClient()

try:
    # Download the data as a string
    data = client.DownloadString('https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8/processes')
    
    # Save raw XML content to a file for inspection (if necessary)
    # Make sure to specify the correct path where the script has write permissions
    with open('C:\\path\\to\\your\\directory\\raw_xml_output.xml', 'w') as file:
        file.write(data)
    
    # Parse the XML response
    root = ET.fromstring(data)

    # Now you can iterate over the elements and extract data
    for process in root.findall('{http://www.ilcd-network.org/ILCD/ServiceAPI}process'):
        # Extract details here
        # Make sure to replace this comment with actual parsing code

except ET.ParseError as pe:
    print("Failed to parse XML: {0}".format(pe))
except Exception as e:
    print("Failed to fetch materials: {0}".format(str(e)))
