import clr
import xml.etree.ElementTree as ET
clr.AddReference('System')
clr.AddReference('System.Net')
from System.Text import Encoding
from System.Net import WebClient

def preprocess_xml_data(data):
    # Replace  with a suitable replacement or remove it
    return data.replace(u"\u2122", "")  # Removing  symbol

def get_api_data(url):
    client = WebClient()
    client.Encoding = Encoding.UTF8
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
            'ns0': 'http://www.ilcd-network.org/ILCD/ServiceAPI/Process',
            'ns3': 'http://www.ilcd-network.org/ILCD/ServiceAPI'
        }

        # Find the first material process
        first_material = root.find('ns0:process', namespaces)

        if first_material is not None:
            uuid = first_material.find('ns3:uuid', namespaces).text
            name = first_material.find('ns3:name[@xml:lang="en"]', namespaces).text
            class_id = first_material.find('ns3:classification/ns3:class[@level="0"]', namespaces).get('classId')

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
