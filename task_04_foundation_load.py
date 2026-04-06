#Задача 4: рабочий график
"""
В этой задаче определяется день недели по номеру и указывается режим работы
"""
#Исходные данные
"""
номер дня 1-7 соответствует дням недели пн-вс
"""
day_number = 5 #вводится число от 1 до 7

#Определение названия дня недели
if day_number == 1:
    day_name = "Понедельник"
elif day_number == 2:
    day_name = "Вторник"
elif day_number == 3:
    day_name = "Среда"
elif day_number == 4:
    day_name = "Четверг"
elif day_number == 5:
    day_name = "Пятница"
elif day_number == 6:
    day_name = "Суббота"
elif day_number == 7:
    day_name = "Воскресенье"
else:
    day_name = "Ошибка: неверный номер дня. Введите число 1-7."

#Определение режима работы
"""
Рабочие дни: 
понедельник - пятница (1-5)
8:00 - начало смены

Выходные: 
суббота, воскресенье (6-7)
Отдых
"""
if 1 <= day_number <= 5:
    work_mode = "8:00 - начало смены"
    day_type = "Рабочий день"
elif 6 <= day_number <= 7:
    work_mode = "Отдых"
    day_type = "Выходной"
else:
    work_mode = "Ошибка"
    day_type = "Ошибка"

#Вывод
print()
print("РАБОЧИЙ ГРАФИК")
print()
print(f"Номер дня: {day_number}")
print(f"День недели: {day_name}")
print(f"Тип дня: {day_type}")
print(f"Режим работы: {work_mode}")