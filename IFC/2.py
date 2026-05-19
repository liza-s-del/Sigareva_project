#Вывод информации по первой стене

"""В консоли отображаются количество стен и краткая информация о первой стене"""

import ifcopenshell

file_path = r"C:\Users\user\Sigareva_project\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Количество стен в модели:", len(walls))

first_wall = walls[0]
print(first_wall)

"""
Количество стен в модели: 24
#20404=IfcWall('0AcubLcjbDbQQeAgLg2Zeu',#48,'Basic Wall:_Bindeingsverk 99mm:374186',$,'Basic Wall:_Bindeingsverk 99mm:372309',#20257,#20402,'374186')
"""