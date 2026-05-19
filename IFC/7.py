# Создание подмодели с отфильтрованными дверями

"""Создаётся отдельный IFC-файл, содержащий только отфильтрованные двери,
и в консоли отображается их количество и проверка соответствия критерию."""

import ifcopenshell
import ifcopenshell.api

file_path = r"C:\Users\user\Sigareva_project\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

# Создаём новую пустую модель
new_model = ifcopenshell.api.run("project.create_file", version="IFC4")

doors = model.by_type("IfcDoor")

min_width = 900

filtered_doors = []

for door in doors:
    width = getattr(door, "OverallWidth", None)
    if width is not None and width >= min_width:
        filtered_doors.append(door)

print(f"Критерий: ширина двери >= {min_width} мм")
print(f"Всего дверей в модели: {len(doors)}")
print(f"Отфильтровано дверей: {len(filtered_doors)}")


for door in filtered_doors:
    ifcopenshell.api.run("root.create_entity", new_model, ifc_class="IfcDoor", name=door.Name)

output_path = r"C:\Users\user\Sigareva_project\IFC\doors_wide.ifc"
new_model.write(output_path)

check_model = ifcopenshell.open(output_path)
check_doors = check_model.by_type("IfcDoor")

print(f"\nДверей в подмодели: {len(check_doors)}")

"""
Критерий: ширина двери >= 900 мм
Всего дверей в модели: 6
Отфильтровано дверей: 2

Дверей в подмодели: 2
"""