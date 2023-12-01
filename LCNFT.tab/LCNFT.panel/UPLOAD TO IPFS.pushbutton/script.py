import clr
import os
import json

# .NET references
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
clr.AddReference("System.Windows.Forms")
clr.AddReference("Microsoft.VisualBasic")
clr.AddReference("System.Net")

# Imports
from Autodesk.Revit.UI import TaskDialog
from System.Windows.Forms import OpenFileDialog, DialogResult
from System.Net import WebClient, WebHeaderCollection, WebException
from System.Text import Encoding

# Function to upload file to IPFS using Pinata
def pin_file_to_ipfs(file_path):
    api_endpoint = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    api_key = "93407b953284346d89e2"
    api_secret = "c6153a7e62502c242c7c7415b40bab18fea5dd921457e632a58eab03c194c736"

    client = WebClient()
    client.Headers.Add("pinata_api_key", api_key)
    client.Headers.Add("pinata_secret_api_key", api_secret)

    try:
        response = client.UploadFile(api_endpoint, file_path)
        response_string = Encoding.UTF8.GetString(response)
        return json.loads(response_string)
    except WebException as e:
        return str(e.Response.GetResponseStream().ReadToEnd())


# Main function
def main():
    # Open file dialog to select file
    file_dialog = OpenFileDialog()
    file_dialog.Title = "Select a file to upload to IPFS"
    if file_dialog.ShowDialog() == DialogResult.OK:
        selected_file_path = file_dialog.FileName
        # Upload the selected file to IPFS
        try:
            response = pin_file_to_ipfs(selected_file_path)
            if "IpfsHash" in response:
                TaskDialog.Show(
                    "Success",
                    "File uploaded to IPFS with hash: %s" % response["IpfsHash"],
                )
                print(response["IpfsHash"])
            else:
                TaskDialog.Show("Error", "Failed to upload to IPFS: %s" % response)
        except Exception as e:
            TaskDialog.Show("Error", "Error: {}".format(str(e)))


# Run main function
main()
