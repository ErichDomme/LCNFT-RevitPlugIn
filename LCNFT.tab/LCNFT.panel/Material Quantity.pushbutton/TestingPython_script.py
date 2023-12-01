# coding=utf-8

# Import necessary Revit API classes
from Autodesk.Revit.DB import (
    FilteredElementCollector,
    BuiltInCategory,
    Wall,
    Solid,
    ElementId,
    Options,
)

# Access the current Revit document
doc = __revit__.ActiveUIDocument.Document

# Dictionary to store material data with volume and area
material_data = {}

# Conversion factors
SQFT_TO_SQM = 0.092903  # Square feet to square meters
CFT_TO_CBM = 0.0283168  # Cubic feet to cubic meters

# Traverse through building elements (e.g., walls)
for element in (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Walls)
    .WhereElementIsNotElementType()
):
    # Get the element's geometry
    geo_element = element.get_Geometry(Options())

    for geo_object in geo_element:
        if isinstance(geo_object, Solid):
            # Calculate volume and area
            volume = geo_object.Volume
            area = geo_object.SurfaceArea

            # Convert from square feet to square meters and from cubic feet to cubic meters
            volume_m3 = volume * CFT_TO_CBM
            area_m2 = area * SQFT_TO_SQM

            # Get the materials for the element
            material_ids = element.GetMaterialIds(False)

            for material_id in material_ids:
                material = doc.GetElement(material_id)
                material_name = material.Name

                # If the material is not in the dictionary, add it
                if material_name not in material_data:
                    material_data[material_name] = {"volume": 0, "area": 0}

                # Accumulate volume and area for the material
                material_data[material_name]["volume"] += volume_m3
                material_data[material_name]["area"] += area_m2

# Print the material data with volume and area
for material, data in material_data.items():
    print("Material: {}".format(material))
    print("Volume: {} m³".format(data["volume"]))
    print("Area: {} m²".format(data["area"]))
    print("-----")
