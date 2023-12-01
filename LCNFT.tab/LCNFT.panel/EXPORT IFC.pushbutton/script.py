import clr
import os

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
clr.AddReference("System.Windows.Forms")
clr.AddReference("Microsoft.VisualBasic")

from Autodesk.Revit.DB import IFCExportOptions, IFCVersion, Transaction
from Autodesk.Revit.UI import TaskDialog
from System.Windows.Forms import FolderBrowserDialog, DialogResult
from Microsoft.VisualBasic import Interaction

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
            return None  # User pressed cancel
        complete_path = os.path.join(export_folder, filename + ".ifc")
        if os.path.exists(complete_path):
            TaskDialog.Show(
                "File Exists",
                "A file with this name already exists. Please choose another name.",
            )
            continue
        else:
            return filename


# Main function
def main():
    # Show folder browser dialog to get export path
    folder_browser = FolderBrowserDialog()
    if folder_browser.ShowDialog() == DialogResult.OK:
        export_folder = folder_browser.SelectedPath
        filename = get_filename_from_user(export_folder)

        if filename:
            filename = filename + ".ifc"
            # Export IFC
            try:
                active_doc = __revit__.ActiveUIDocument.Document
                # Start a transaction
                with Transaction(active_doc, "IFC Export") as t:
                    t.Start()
                    export_to_ifc(
                        doc=active_doc, export_folder=export_folder, filename=filename
                    )
                    t.Commit()
                TaskDialog.Show("Success", "IFC Exported Successfully!")
            except Exception as e:
                TaskDialog.Show("Error", "Error exporting IFC: {}".format(str(e)))


# Run main function
main()


# Version 2
# import clr

# clr.AddReference("RevitAPI")
# clr.AddReference("RevitAPIUI")
# clr.AddReference("System.Windows.Forms")
# clr.AddReference("Microsoft.VisualBasic")

# from Autodesk.Revit.DB import IFCExportOptions, IFCVersion, Transaction
# from Autodesk.Revit.UI import TaskDialog
# from System.Windows.Forms import FolderBrowserDialog, DialogResult
# from Microsoft.VisualBasic import Interaction

# # Function to export IFC
# def export_to_ifc(doc, export_folder, filename):
#     ifc_options = IFCExportOptions()
#     ifc_options.FileVersion = IFCVersion.IFC2x3
#     doc.Export(export_folder, filename, ifc_options)


# # Function to get filename from user
# def get_filename_from_user():
#     default_filename = "Model"
#     prompt_text = "Enter desired filename for the IFC export (without extension):"
#     title = "Filename"
#     filename = Interaction.InputBox(prompt_text, title, default_filename)
#     return filename


# # Main function
# def main():
#     # Show folder browser dialog to get export path
#     folder_browser = FolderBrowserDialog()
#     if folder_browser.ShowDialog() == DialogResult.OK:
#         export_folder = folder_browser.SelectedPath
#         filename = get_filename_from_user()

#         if filename:
#             filename = filename + ".ifc"
#             # Export IFC
#             try:
#                 active_doc = __revit__.ActiveUIDocument.Document
#                 # Start a transaction
#                 with Transaction(active_doc, "IFC Export") as t:
#                     t.Start()
#                     export_to_ifc(
#                         doc=active_doc, export_folder=export_folder, filename=filename
#                     )
#                     t.Commit()
#                 TaskDialog.Show("Success", "IFC Exported Successfully!")
#             except Exception as e:
#                 TaskDialog.Show("Error", "Error exporting IFC: {}".format(str(e)))


# # Run main function
# main()


# Version 01
# import clr

# clr.AddReference("RevitAPI")
# clr.AddReference("RevitAPIUI")
# clr.AddReference("System.Windows.Forms")

# from Autodesk.Revit.DB import IFCExportOptions, IFCVersion, Transaction
# from Autodesk.Revit.UI import TaskDialog
# from System.Windows.Forms import FolderBrowserDialog, DialogResult

# # Function to export IFC
# def export_to_ifc(doc, export_folder, filename):
#     ifc_options = IFCExportOptions()
#     ifc_options.FileVersion = IFCVersion.IFC2x3
#     doc.Export(export_folder, filename, ifc_options)


# # Main function
# def main():
#     # Show folder browser dialog to get export path
#     folder_browser = FolderBrowserDialog()
#     if folder_browser.ShowDialog() == DialogResult.OK:
#         export_folder = folder_browser.SelectedPath
#         filename = "model.ifc"

#         # Export IFC
#         try:
#             active_doc = __revit__.ActiveUIDocument.Document
#             # Start a transaction
#             with Transaction(active_doc, "IFC Export") as t:
#                 t.Start()
#                 export_to_ifc(
#                     doc=active_doc, export_folder=export_folder, filename=filename
#                 )
#                 t.Commit()
#             TaskDialog.Show("Success", "IFC Exported Successfully!")
#         except Exception as e:
#             TaskDialog.Show("Error", "Error exporting IFC: {}".format(str(e)))


# # Run main function
# main()
