# Упражнение по программированию
# Глава 3. Страница 172. Упражнение №2 - Сравнение площади прямоугольников

# Параметры первого прямоугольника
lenghtRectFirst = float(input('Введите длину первого прямоугольника: '))
widthRectFirst = float(input('Введите ширину первого прямоугольника: '))
print('\n')

# Параметры второго прямоугольника
lenghtRectSecond = float(input('Введите длину второго прямоугольника: '))
widthRectSecond = float(input('Введите ширину второго прямоугольника: '))
print('\n')

# Вычисление площадей прямоугольников
SquareFirst = lenghtRectFirst * widthRectFirst
SquareSecond = lenghtRectSecond * widthRectSecond

# Печать площадей прямоугольников
print(f'Площадь первого прямоугольника: {SquareFirst:.2f}')
print(f'Площадь второго прямоугольника: {SquareSecond:.2f}\n')

# Сравнение площадей прямоугольников
if SquareFirst > SquareSecond:
    print('Первый прямоугольник БОЛЬШЕ второго!')
elif SquareFirst < SquareSecond:
    print('Второй прямоугольник БОЛЬШЕ первого!')
elif SquareFirst == SquareSecond:
    print('Прямоугольники РАВНЫ!')
