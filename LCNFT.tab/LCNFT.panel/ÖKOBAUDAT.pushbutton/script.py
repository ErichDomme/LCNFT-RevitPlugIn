import clr
import xml.etree.ElementTree as ET
clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Net')
from System.Text import Encoding
from System.Net import WebClient
from System.Windows.Forms import Application, Form, CheckedListBox, Button, DockStyle

def preprocess_xml_data(data):
    data = data.replace(u"\u2122", "")  # Removing "trademark" symbol
    data = data.replace(u"\u00AE", "")  # Removing "registered" symbol
    return data

def get_api_data(url):
    client = WebClient()
    client.Encoding = Encoding.UTF8
    try:
        data = client.DownloadString(url)
        return preprocess_xml_data(data)
    except Exception as e:
        print("Error fetching data: {0}".format(str(e)))
        return None

def parse_materials(data):
    materialsByClass = {}
    try:
        root = ET.fromstring(data)
        namespaces = {
            'ns0': 'http://www.ilcd-network.org/ILCD/ServiceAPI/Process',
            'ns3': 'http://www.ilcd-network.org/ILCD/ServiceAPI'
        }

        for material in root.findall('ns0:process', namespaces):
            uuid_elem = material.find('ns3:uuid', namespaces)
            uuid = uuid_elem.text if uuid_elem is not None else "UUID not found"

            name_elem = material.find('ns3:name', namespaces)
            name = name_elem.text if name_elem is not None else "Name not found"

            class_elem = material.find('ns3:classification/ns3:class[@level="0"]', namespaces)
            class_name = class_elem.text if class_elem is not None else "Class name not found"

            if class_name not in materialsByClass:
                materialsByClass[class_name] = []
            materialsByClass[class_name].append({"name": name, "uuid": uuid})
    except Exception as e:
        print("Error parsing XML: {0}".format(str(e)))

    return materialsByClass

class MaterialSelectionForm(Form):
    def __init__(self, materialsByClass):
        self.Text = "Select Materials"
        self.Width = 800
        self.Height = 400

        self.checkedListBox = CheckedListBox()
        self.checkedListBox.Dock = DockStyle.Fill
        self.checkedListBox.CheckOnClick = True

        self.populate_materials(materialsByClass)

        # Add select all button
        self.selectAllButton = Button()
        self.selectAllButton.Text = 'Select All'
        self.selectAllButton.Dock = DockStyle.Top
        self.selectAllButton.Click += self.select_all_clicked

        # Add deselect all button
        self.deselectAllButton = Button()
        self.deselectAllButton.Text = 'Deselect All'
        self.deselectAllButton.Dock = DockStyle.Top
        self.deselectAllButton.Click += self.deselect_all_clicked

        self.okButton = Button()
        self.okButton.Text = 'OK'
        self.okButton.Dock = DockStyle.Bottom
        self.okButton.Click += self.button_clicked

        self.Controls.Add(self.checkedListBox)
        self.Controls.Add(self.selectAllButton)
        self.Controls.Add(self.deselectAllButton)
        self.Controls.Add(self.okButton)

    def populate_materials(self, materialsByClass):
        for className, materials in materialsByClass.items():
            for material in materials:
                item = "{0} - {1} ({2})".format(className, material['name'], material['uuid'])
                self.checkedListBox.Items.Add(item)

    def select_all_clicked(self, sender, args):
        for i in range(self.checkedListBox.Items.Count):
            self.checkedListBox.SetItemChecked(i, True)

    def deselect_all_clicked(self, sender, args):
        for i in range(self.checkedListBox.Items.Count):
            self.checkedListBox.SetItemChecked(i, False)

    def button_clicked(self, sender, args):
        selected_materials = [self.checkedListBox.Items[i] for i in range(self.checkedListBox.Items.Count) if self.checkedListBox.GetItemChecked(i)]
        print(selected_materials)  # For testing purposes
        self.Close()

def main():
    url = 'https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8/processes'
    xml_data = get_api_data(url)
    if xml_data:
        materialsByClass = parse_materials(xml_data)
        form = MaterialSelectionForm(materialsByClass)
        Application.Run(form)

main()
