import xml.etree.ElementTree as ET

# Sample XML string (replace this with the actual XML response)
xml_data = '''<sapi:dataSetList xmlns:sapi="http://www.ilcd-network.org/ILCD/ServiceAPI">...</sapi:dataSetList>'''

# Parse the XML
root = ET.fromstring(xml_data)

# Define your namespaces
namespaces = {
    'sapi': 'http://www.ilcd-network.org/ILCD/ServiceAPI',
    # Add other namespaces as needed
}

# Iterate through each dataset
for dataset in root.findall('sapi:process', namespaces):
    # Extract the necessary information
    uuid = dataset.find('sapi:uuid', namespaces).text
    names = dataset.findall('sapi:name', namespaces)
    for name in names:
        lang = name.attrib['{http://www.w3.org/XML/1998/namespace}lang']
        value = name.text
        print(f"Name ({lang}): {value}")
    # Extract other attributes as needed
