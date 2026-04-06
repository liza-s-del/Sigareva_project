#Задача 9: очистка адресов
"""
В этом задании адреса объектов приводятся к стандартному формату
"""
#Исходные адреса
addresses = [
    " г. Москва, ул. Ленина, д.  10 ",
    "г.Казань,ул.Баумана,д.15",
    " г. Санкт-Петербург, ул. Невский, д. 100 "
]


def clean_address(address):
    """
    Функция для очистки и форматирования адреса

    Приводит адрес к стандартному формату:
    - удаляет лишние пробелы в начале и конце
    - добавляет пробелы после сокращений (г., ул., д.)
    - добавляет пробелы после запятых

    :param address: строка с адресом

    return: отформатированная строка адреса
    """
    address = address.strip() #удаляет пробелы в начале и в конце

    #Добавление пробелов после сокращений
    address = address.replace("г.", "г. ")
    address = address.replace("ул.", "ул. ")
    address = address.replace("д.", "д. ")

    address = address.replace(",", ", ") #добавляет пробел после запятой

    while "  " in address:
        address = address.replace("  ", " ") #убирает двойные пробелы

    return address

#Вывод результатов
print()
print("ОЧИСТКА АДРЕСОВ")
print()
print("\n=== СРАВНЕНИЕ ===\n")

for i, addr in enumerate(addresses, start=1):
    cleaned = clean_address(addr)
    print(f"#{i}")
    print(f"ДО: '{addr}'")
    print(f"ПОСЛЕ: '{cleaned}'")