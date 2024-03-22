rubles = int(input('Цена пирожка:\nРублей: '))
kopeyki = int(input('Копеек: '))
value = int(input('Количество пирожков: '))

kop = (kopeyki*value)%100
rub = (kopeyki*value)//100 + (rubles*value)

print(f'Всего {rub} рублей и {kop} копеек.')