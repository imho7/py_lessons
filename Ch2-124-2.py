#Вводим плановую сумму объёма продаж
planSumSales = float(input('Введите плановую сумму объёма продаж: '))
PERCENT_SALES = 0.23 #Планируемый процент прибыли от объёма продаж
planProfit = planSumSales * PERCENT_SALES
print(f"Планируемая прибыль: {planProfit:1,.2f}")
