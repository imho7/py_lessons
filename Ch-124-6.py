# Страница 124 Упражнение 6 Налог с продаж

QuantitySale = float(input('Ведите величину покупки: '))

FED_TAX = 0.05
REG_TAX = 0.025

QFed_tax = QuantitySale * FED_TAX
QReg_tax = QuantitySale * REG_TAX

Sale = QuantitySale + (QuantitySale * (FED_TAX + REG_TAX))

print(f'Федеральный налог составляет: {QFed_tax:.2f}')

print(f'Региональный налог составляет: {QReg_tax:.2f}')

print(f'Общая сумма налога составляет: {QFed_tax + QReg_tax:.2f}')

print(f'общая сумма продажи, включая все налоги составляет: {Sale:.2f}')


