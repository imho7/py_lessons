# Глава 3 Страинца 173 Упражнение 5 Масса и вес

mass = float(input('Введите массу тела: '))
G = 9.8 # Коэффициент свободного падения в м/с*2
weight = mass * G
print(f'Вес составляет {weight:,.2f}H')
if weight > 500:
    print('Вес слишком большой!')
elif weight < 100:
    print('Вес слишком маленький')
else:
    print('Вес нормальный!')
