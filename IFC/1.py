#Подсчет количества стен в модели

"""При запуске скрипта в консоль выводится количество стен в модели"""

import ifcopenshell

file_path = r"C:\Users\user\Sigareva_project\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Количество стен в модели:", len(walls))

"""Количество стен в модели: 24"""