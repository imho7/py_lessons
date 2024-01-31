# Глава 2 Страница 124 Упражнение 4
# Расчёт Общего объёма продаж
cost1 = float(input(f'Введите стоимость товара 1: '))
cost2 = float(input(f'Введите стоимость товара 2: '))
cost3 = float(input(f'Введите стоимость товара 3: '))
cost4 = float(input(f'Введите стоимость товара 4: '))
cost5 = float(input(f'Введите стоимость товара 5: '))

summ = cost1 + cost2 + cost3 + cost4 + cost5

summ_nalog = summ * 0.07

summ_itog = summ + summ_nalog

print (f'Накопленная сумма стоимости товаров составляет: {summ:.2f}')
print (f'Налог с продаж составляет: {summ_nalog:.2f}')
print (f'Итогова сумма составляет: {summ_itog:.2f}')
