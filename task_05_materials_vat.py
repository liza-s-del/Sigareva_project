#Задача 5: Калькулятор скидки
"""
В этой задаче рассчитывается стоимость покупки материалов с прогрессивной системой скидок
"""
#Исходные данные
price = 200 #цена за единицу товара, руб
quantity = 30 #количество товара

#Цена без скидки
total = price * quantity

#Определение скидки
"""
Система скидок:
< 1000₽ → 0%
1000-5000₽ → 5%
> 5000₽ → 10%
"""
if total < 1000:
    discount_percent = 0
    discount_level = "менее 1000₽"
elif total <= 5000:
    discount_percent = 5
    discount_level = "1000-5000₽"
else:
    discount_percent = 10
    discount_level = "более 5000₽"

#Рассчет скидки и итоговой стоимости
discount = total * discount_percent / 100
total_with_discount = total - discount
