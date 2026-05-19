#Получение этажей и информации о модели

"""Скрипт показывает схему IFC, количество этажей и список этажей с их отметками"""

import ifcopenshell

file_path = r"C:\Users\user\Sigareva_project\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

storeys = model.by_type("IfcBuildingStorey")
print("Схема IFC:", model.schema)
print("Количество этажей:", len(storeys))

for storey in storeys:
    name = storey.Name
    elevation = storey.Elevation or "None"
    print(f"Этаж: {name}, Elevation={elevation}")

print("\nTITLE: Информация об этажах модели")

"""
Схема IFC: IFC2X3
Количество этажей: 3
Этаж: 0. kjeller, Elevation=-800.0
Этаж: 1. etasje, Elevation=None
Этаж: 2. etasje, Elevation=2850.0

TITLE: Информация об этажах модели
"""