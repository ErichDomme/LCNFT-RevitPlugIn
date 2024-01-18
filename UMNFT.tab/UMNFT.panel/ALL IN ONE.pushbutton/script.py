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
from Autodesk.Revit.DB import IFCExportOptions, IFCVersion, Transaction
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogResult
from System.Windows.Forms import FolderBrowserDialog, DialogResult
from Microsoft.VisualBasic import Interaction
from System.Net import WebClient, WebHeaderCollection, WebException
from System.Text import Encoding
from System.IO import StreamReader


# Function to export IFC
def export_to_ifc(doc, export_folder, filename):
    ifc_options = IFCExportOptions()
    ifc_options.FileVersion = IFCVersion.IFC2x3
    doc.Export(export_folder, filename, ifc_options)


# Function to get filename from user
def get_filename_from_user(export_folder):
    while True:
        default_filename = "model"
        prompt_text = "Enter desired filename for the IFC export (without extension):"
        title = "Filename"
        filename = Interaction.InputBox(prompt_text, title, default_filename)
        if not filename:
            return None
        complete_path = os.path.join(export_folder, filename + ".ifc")
        if os.path.exists(complete_path):
            TaskDialog.Show(
                "File Exists",
                "A file with this name already exists. Please choose another name.",
            )
            continue
        else:
            return filename


# Function to upload file to IPFS using Pinata
def pin_file_to_ipfs(file_path):
    api_endpoint = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    api_key = "fc43276cd57681197751"  # Placeholder for your API Key
    api_secret = "1b223b21260b64d56c8071d87fa82d1d8bef75dd0456e60ca05da9406ddb37ad"  # Placeholder for your API Secret

    client = WebClient()
    client.Headers.Add("pinata_api_key", api_key)
    client.Headers.Add("pinata_secret_api_key", api_secret)

    try:
        response = client.UploadFile(api_endpoint, file_path)
        response_string = Encoding.UTF8.GetString(response)
        return json.loads(response_string)
    except WebException as e:
        if e.Response is not None:
            response_stream = e.Response.GetResponseStream()
            reader = StreamReader(response_stream)
            response_text = reader.ReadToEnd()
            return response_text
        else:
            return str(e)



# Function to ask user if they want to retain local file
def user_wants_local_copy():
    result = TaskDialog.Show(
        "Retain Local File",
        "Do you want to keep the local IFC file?",
        TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.No,
    )
    return result == TaskDialogResult.Yes


# Main function
def main():
    folder_browser = FolderBrowserDialog()
    if folder_browser.ShowDialog() == DialogResult.OK:
        export_folder = folder_browser.SelectedPath
        filename = get_filename_from_user(export_folder)

        if filename:
            filename_with_ext = filename + ".ifc"
            try:
                active_doc = __revit__.ActiveUIDocument.Document
                with Transaction(active_doc, "IFC Export") as t:
                    t.Start()
                    export_to_ifc(
                        doc=active_doc,
                        export_folder=export_folder,
                        filename=filename_with_ext,
                    )
                    t.Commit()

                response = pin_file_to_ipfs(
                    os.path.join(export_folder, filename_with_ext)
                )
                if "IpfsHash" in response:
                    TaskDialog.Show(
                        "Success",
                        "IFC Exported and uploaded to IPFS with hash: %s"
                        % response["IpfsHash"],
                    )
                    print(response["IpfsHash"])

                    if not user_wants_local_copy():
                        try:
                            os.remove(os.path.join(export_folder, filename_with_ext))
                        except Exception as e:
                            TaskDialog.Show(
                                "Error",
                                "Failed to delete local file. Error: %s" % str(e),
                            )
                else:
                    TaskDialog.Show("Error", "Failed to upload to IPFS: %s" % response)
            except Exception as e:
                TaskDialog.Show("Error", "Error: %s" % str(e))


main()