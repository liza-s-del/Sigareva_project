#Анализ размеров дверей и поиск "узких дверей"

"""В консоли отображается список дверей, не удовлетворяющих минимальной требуемой
ширине, и общее количество таких дверей"""

import ifcopenshell

file_path = r"C:\Users\user\Sigareva_project\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")

min_width = 900
narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)

    if width is not None and width < min_width:
        narrow_doors.append((name, width, height))

for name, width, height in narrow_doors:
    print("Дверь:", name, "Ширина", round(width), "Высота", height)

print('\nКоличество "узких" дверей:', len(narrow_doors))

"""
Дверь: M_Single-Flush:_800x2000mm:379349 Ширина 800 Высота 2000.0
Дверь: M_Single-Flush:_800x2000mm:379616 Ширина 800 Высота 2000.0
Дверь: M_Single-Flush:_800x2000mm:384449 Ширина 800 Высота 2000.0
Дверь: M_Single-Flush:_800x2000mm:384451 Ширина 800 Высота 2000.0

Количество "узких" дверей: 4
"""