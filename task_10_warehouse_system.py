#Задача 10: система учета склада
"""
В данном задании создана система учета материалов с контролем критических остатков
"""
#Исходные данные:
"""
Cловарь с вложенными словарями
Структура: материал -> {количество, цена, минимальный остаток}
"""
warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

#Вывод таблицы материалов
print("=" * 70)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 70)
print(f"\n{'Материал':<12} {'Кол-во':<8} {'Цена':<10} {'Мин.':<8} {'Стоимость':<12}")
print("-" * 70)

total_warehouse_cost = 0
critical_materials = []

for material, data in warehouse.items():
    quantity = data["quantity"]
    price = data["price"]
    min_qty = data["min_quantity"]
    cost = quantity * price
    total_warehouse_cost += cost

    # Проверка на критический остаток
    is_critical = quantity < min_qty

    if is_critical:
        critical_mark = " КРИТИЧ!"
    else:
        critical_mark = ""

    if is_critical:
        critical_materials.append((material, quantity, min_qty))

    print(f"{material:<12} {quantity:<8} {price:<10.2f} {min_qty:<8} {cost:<12.2f}{critical_mark}")
print("=" * 70)
print(f"{'ОБЩАЯ СТОИМОСТЬ:':<40} {total_warehouse_cost:<12.2f} руб")

#Самый дорогой материал
def find_most_expensive(warehouse_dict):
    """
    Находит самый дорогой материал на складе.

    :param warehouse_dict: словарь со складом
    return: название материала и его стоимость
    """
    most_expensive_name = None
    max_cost = 0

    for material, data in warehouse_dict.items():
        cost = data["quantity"] * data["price"]
        if cost > max_cost:
            max_cost = cost
            most_expensive_name = material

    return most_expensive_name, max_cost

# Вызов функции
most_expensive_name, max_cost = find_most_expensive(warehouse)

print(f"Самый дорогой материал: {most_expensive_name} ({max_cost:.2f} руб)")
