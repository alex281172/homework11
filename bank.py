def banks():
    with open('accaunt.txt', 'r') as f:
        accaunt = int(f.read())

    pay_history = []

    while True:
        print(f'{"*" * 18} ВАШ КОШЕЛЕК {"*" * 18} ')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('-' * 50)
        print(f'На счете {accaunt} руб.')
        print('-' * 50)

        choice = input('Выберите пункт меню Мой банковский счет -> ')
        if choice == '1':
            while True:
                try:
                    accaunt = accaunt + int(input('пополните счет: '))
                    with open('accaunt.txt', 'w') as f:
                        accaunt_str = str(accaunt)
                        f.write(accaunt_str)
                    print(f'На счете {accaunt} руб.')
                    break
                except ValueError:
                    print('введите число')
        elif choice == '2':
            while True:
                try:
                    pay = int(input('введите сумму покупки: '))
                    if accaunt >= pay:
                        pay_object = input('что покупаете? ')
                        accaunt -= pay
                        # pay_history.append((pay_object, pay))
                        with open('history_oder.txt', 'a', encoding='utf-8') as f:
                            f.write(f'{pay_object, pay}\n')
                        print(f'Вы купили \'{pay_object}\' за {pay}руб.')
                        break
                    else:
                        print('Средств недостаточно')
                except ValueError:
                    print('введите число')
        elif choice == '3':
            print('*' * 50)
            print('История покупок:')
            # for counter in pay_history:
            #     print(*counter)
            with open('history_oder.txt', 'r', encoding='utf-8') as f:
                list = f.read()
                print(list)
            print('-' * 50)
            print(f'На счете {accaunt} руб.')
            print('*' * 50)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
if __name__ == '__main__':
    banks()

