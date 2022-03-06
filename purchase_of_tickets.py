price_all = 0  # принимаем начальную стоимость услуги
while True:
    try:
        ticket_number = input('Добро пожаловать на онлайн-конференцию!\nВведите необходимое количество билетов:\n')
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break  # возврат, пока не будут введены корректные для программы данные
    except ValueError:  # выявление неверных данных
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age_for_ticket = int(input(f'Введите возраст участника для билета №{i}? '))
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 18 <= age_for_ticket < 25:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            elif 25 < age_for_ticket <= 122:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.\n'
                      'Поздравляем Вас! Возраст участника превышает мировой рекорд долгожительства, \n '
                      'установленный в 1997 году Жанной Луизой Кальман!\n Пожалуйста, обратитесь в нашу Администрацию.')

            if type(age_for_ticket) == int:
                break  # возврат, пока не будут введены корректные для программы данные
        except ValueError:  # выявление неверных данных
            print('Введите полное количество лет')
if ticket_number > 3 and price_all > 0:  # стоимость заказа должна быть больше нуля
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} руб. \n с учетом 10%-ой скидки на полную стоимость заказа за \n '
          f'регистрацию больше 3-х человек')
elif ticket_number > 3 and price_all == 0:  # если стоимость заказа равна нулю
    print(f'Сумма к оплате составляет {price_all} руб.')
else:
    print(f'Сумма к оплате {price_all} руб.')
