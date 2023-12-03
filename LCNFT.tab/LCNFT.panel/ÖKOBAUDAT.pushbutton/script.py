import clr
import xml.etree.ElementTree as ET
clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Net')
from System.Text import Encoding
from System.Net import WebClient
from System.Windows.Forms import Application, Form, TreeView, TreeNode, Button, DockStyle

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
        self.Height = 600

        self.treeView = TreeView()
        self.treeView.Dock = DockStyle.Fill
        self.treeView.CheckBoxes = True
        self.treeView.AfterCheck += self.treeView_AfterCheck

        self.populate_tree(materialsByClass)

        self.okButton = Button()
        self.okButton.Text = 'OK'
        self.okButton.Dock = DockStyle.Bottom
        self.okButton.Click += self.button_clicked

        self.Controls.Add(self.treeView)
        self.Controls.Add(self.okButton)

    def populate_tree(self, materialsByClass):
        for className, materials in materialsByClass.items():
            parent_node = TreeNode(className)
            self.treeView.Nodes.Add(parent_node)
            for material in materials:
                child_node = TreeNode("{0} ({1})".format(material['name'], material['uuid']))
                parent_node.Nodes.Add(child_node)

    def treeView_AfterCheck(self, sender, e):
        for node in e.Node.Nodes:
            node.Checked = e.Node.Checked  # Check/uncheck all child nodes.

    def button_clicked(self, sender, args):
        selected_materials = []
        for class_node in self.treeView.Nodes:
            for material_node in class_node.Nodes:
                if material_node.Checked:
                    selected_materials.append(material_node.Text)
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
