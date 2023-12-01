# Import necessary Revit API classes
import json
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Wall

# Access the current Revit document
doc = __revit__.ActiveUIDocument.Document

# Create a dictionary to store material data
material_data = {}

# Traverse through building elements
for element in (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Walls)
    .WhereElementIsNotElementType()
):  # Example for walls
    if isinstance(element, Wall):  # Check if the element is a Wall
        wall_type = element.WallType
        compound_structure = wall_type.GetCompoundStructure()

        if compound_structure:  # Check if the wall has a compound structure
            for layer in compound_structure.GetLayers():
                material_id = layer.MaterialId
                material = doc.GetElement(material_id)

                if material:
                    # Extract desired properties
                    material_name = material.Name

                    # Extract color
                    color = material.Color
                    if color:
                        color_value = (color.Red, color.Green, color.Blue)
                    else:
                        color_value = "N/A"

                    # Extract shininess and transparency
                    appearance_asset = material.AppearanceAssetId
                    if appearance_asset.IntegerValue > 0:
                        appearance_asset_element = doc.GetElement(appearance_asset)

                        # Navigate through the appearance properties
                        asset = appearance_asset_element.GetRenderingAsset()
                        shininess_property = asset.FindByName("generic_shininess")
                        transparency_property = asset.FindByName("generic_transparency")

                        shininess = (
                            shininess_property.Value if shininess_property else "N/A"
                        )
                        transparency = (
                            transparency_property.Value
                            if transparency_property
                            else "N/A"
                        )
                    else:
                        shininess = "N/A"
                        transparency = "N/A"

                    # Store the data in the dictionary
                    material_data[material_name] = {
                        "color": color_value,
                        "shininess": shininess,
                        "transparency": transparency,
                    }


print("-" * 60)
print(
    "{:<30} {:<10} {:<10} {:<10}".format(
        "Material", "Color", "Transparency", "Shininess"
    )
)
print("-" * 60)
for material, properties in material_data.items():
    color = properties["color"] if properties["color"] != "N/A" else "N/A"
    transparency = (
        properties["transparency"] if properties["transparency"] != "N/A" else "N/A"
    )
    shininess = properties["shininess"] if properties["shininess"] != "N/A" else "N/A"
    print(
        "{:<30} {:<10} {:<10} {:<10}".format(
            material, str(color), str(transparency), str(shininess)
        )
    )
print("-" * 60)
