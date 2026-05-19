#Изменение свойства стены и сохранение новой модели

"""Создается новый IFC-файл с измененным именем первой стены и
обновленным свойством в ее наборе свойств."""

import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.api

file_path = r"C:\Users\user\Sigareva_project\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")

first_wall = walls[0]

print("Исходные свойства")
print("  Name:", first_wall.Name)
print("  ObjectType:", getattr(first_wall, "ObjectType", None))

first_wall.Name = "MODIFIED_" + (first_wall.Name or "Wall")

pset_entity = next((
    rel.RelatingPropertyDefinition for rel in first_wall.IsDefinedBy
    if rel.is_a("IfcRelDefinesByProperties")
    and rel.RelatingPropertyDefinition.is_a("IfcPropertySet")
    and rel.RelatingPropertyDefinition.Name == "Pset_WallCommon"
), None)

ifcopenshell.api.run("pset.edit_pset", model, pset=pset_entity, properties={"IsExternal": True})

output_path = r"C:\Users\user\Sigareva_project\IFC\modified.ifc"
model.write(output_path)

new_model = ifcopenshell.open(output_path)
new_walls = new_model.by_type("IfcWall")
new_first_wall = new_walls[0]

print("\nОбновленные данные")
print("  Name:", new_first_wall.Name)

new_psets = ifcopenshell.util.element.get_psets(new_first_wall)
if "Pset_WallCommon" in new_psets:
    print("  IsExternal из Psets:", new_psets["Pset_WallCommon"].get("IsExternal"))

"""
Исходные свойства
  Name: Basic Wall:_Bindeingsverk 99mm:374186
  ObjectType: Basic Wall:_Bindeingsverk 99mm:372309

Обновленные данные
  Name: MODIFIED_Basic Wall:_Bindeingsverk 99mm:374186
  IsExternal из Psets: True
"""