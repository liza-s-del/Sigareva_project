#Задача 2: Параметры помещения
"""
В задаче рассчитываются геометрические параметры помещения и стоимость покраски стен
"""

"""
Исходные данные
:param length: длина помещения, м
:param width: ширина помещения, м
:param height: высота помещения, м
"""
length = 8.0
width = 6.0
height = 2.7
Per_square_metre_price = 125.0

"""
Рассчет геометрических параметров
:param floor_area: площадь пола, м2
:param wall_area: площадь стен, м2
:param volume: объем помещения, м3
"""
floor_area = length * width
wall_area = 2 * (length + width) * height
volume = length * width * height