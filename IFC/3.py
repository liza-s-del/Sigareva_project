#Чтение наборов свойств стены

"""В консоль выводится перечень всех Pset и всех свойств для первой стены"""

import ifcopenshell
import ifcopenshell.util.element

file_path = r"C:\Users\user\Sigareva_project\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Количество стен в модели:", len(walls))

first_wall = walls[0]
print(first_wall)

psets = ifcopenshell.util.element.get_psets(first_wall)
print(psets)

for pset_name, props in psets.items():
    print("Pset:", pset_name)

    for prop_name, value in props.items():
        print("  ",prop_name, "=", value)

"""
Количество стен в модели: 24
#20404=IfcWall('0AcubLcjbDbQQeAgLg2Zeu',#48,'Basic Wall:_Bindeingsverk 99mm:374186',$,'Basic Wall:_Bindeingsverk 99mm:372309',#20257,#20402,'374186')
{'Pset_WallCommon': {'IsExternal': False, 'ExtendToStructure': True, 'Reference': '_Bindeingsverk 99mm', 'LoadBearing': False, 'ThermalTransmittance': 0.470430107526882, 'id': 20409}}
Pset: Pset_WallCommon
   IsExternal = False
   ExtendToStructure = True
   Reference = _Bindeingsverk 99mm
   LoadBearing = False
   ThermalTransmittance = 0.470430107526882
   id = 20409
"""