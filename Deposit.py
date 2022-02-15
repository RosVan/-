
money_ТКБ = int(input('Банк "ТКБ" Введите сумму:'))
money_СКБ = int(input('Банк "ТКБ" Введите сумму:'))
money_ВТБ = int(input('Банк "ТКБ" Введите сумму:'))
money_СБЕР = int(input('Банк "ТКБ" Введите сумму:'))
money_all = [money_ТКБ, money_СКБ, money_ВТБ, money_СБЕР]

print(money_all)

per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
deposit = []

for key in per_cent:
    per_cent[key] = money_all[0] * per_cent[key] /100
    deposit.append(round(per_cent[key], 2))

print (deposit)
print (max(deposit))
print (min(deposit))