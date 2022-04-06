accaunt = 0
pay_history = []
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'На счете {accaunt} руб.')

    choice = input('Выберите пункт меню -> ')
    if choice == '1':
        accaunt = accaunt + int(input('пополните счет: '))
        print(f'На счете {accaunt} руб.')
    elif choice == '2':
        pay = int(input('введите суммы покупки: '))
        if pay < accaunt:
            pay_object = input('что покупаете? ')
            accaunt -= pay
            pay_history.append((pay_object, pay))
        else:
            print('Средств недостаточно')
    elif choice == '3':
        print('История покупок:')
        for counter in pay_history:
            print(*counter)
        print(f'На счете {accaunt} руб.')
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')