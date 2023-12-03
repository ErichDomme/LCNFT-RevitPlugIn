import clr
import xml.etree.ElementTree as ET
clr.AddReference('System.Net')
clr.AddReference('mscorlib')  # Adding reference to mscorlib which contains System namespace
from System import Text  # Importing Text from System namespace
from System.Net import WebClient

def preprocess_xml_data(data):
    # Replace  with a suitable replacement or remove it
    return data.replace(u"\u2122", "")  # Removing  symbol

def get_api_data(url):
    client = WebClient()
    client.Encoding = Text.Encoding.UTF8  # Set UTF-8 encoding directly
    try:
        data = client.DownloadString(url)
        # Preprocess the data to handle special characters
        processed_data = preprocess_xml_data(data)
        return processed_data
    except Exception as e:
        print("Error fetching data: {0}".format(str(e)))
        return None

def parse_xml_and_print(data):
    try:
        root = ET.fromstring(data)
        namespaces = {
            'sapi': 'http://www.ilcd-network.org/ILCD/ServiceAPI',  # add other namespaces if needed
        }

        # Find the first material process
        first_material = root.find('sapi:process', namespaces)
        if first_material is not None:
            uuid = first_material.find('sapi:uuid', namespaces).text
            name = first_material.find('sapi:name', namespaces).text
            class_id = first_material.find('sapi:classification/sapi:class[@level="0"]', namespaces).get('classId')

            # Print the extracted information
            print("UUID: {0}, Name: {1}, Class ID at level 0: {2}".format(uuid, name, class_id))
        else:
            print("No material found")

    except Exception as e:
        print("Error parsing XML: {0}".format(str(e)))

def main():
    url = 'https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8/processes'
    xml_data = get_api_data(url)
    if xml_data:
        parse_xml_and_print(xml_data)

# Run the main function
main()
