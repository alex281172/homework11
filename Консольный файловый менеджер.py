import os
import shutil
import sys
import shutil
import turtle





while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной систем')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. Черепашка')
    print('13. выход')


    choice = input('Выберите пункт меню -> ')
    if choice == '1':
        print(f'{"*" * 18} СОЗДАНИЕ ПАПКИ {"*" * 18} ')
        while True:
            name_folder = input('укажите название папки для создания: ')
            if not os.path.exists(name_folder):
                os.mkdir(f'{name_folder}')
                print(f'папка \'{name_folder}\' создана')
                print('*' * 51)
                break
            else:
                print(f'папка \'{name_folder}\' существует')
                print('*' * 51)
                break
    elif choice == '2':
        print(f'{"*" * 18} УДАЛЕНИЕ ПАПКИ/ФАЙЛА {"*" * 18} ')
        while True:
            choise = int(input('удалить папку - укажите \'1\', удалить файл - - укажите \'2\': '))
            if choise == 1:
                print(f'{"*" * 18} УДАЛЕНИЕ ПАПКИ {"*" * 18} ')
                name_folder = input('укажите название папки для удаления: ')
                if os.path.exists(name_folder):
                    os.rmdir(f'{os.getcwd()}\{name_folder}')
                    print(f'папка \'{name_folder}\' удалена')
                    print('*' * 51)
                    break
                else:
                    print(f'папка \'{name_folder}\' не существует')
                    print('*' * 51)
                    break
            if choise == 2:
                print(f'{"*" * 18} УДАЛЕНИЕ ФАЙЛА {"*" * 18} ')
                name_folder = input('укажите название файла для удаления: ')
                if os.path.exists(name_folder):
                    os.remove(f'{os.getcwd()}\{name_folder}')
                    print(f'файл \'{name_folder}\' удален')
                    print('*' * 51)
                    break
                else:
                    print(f'файл \'{name_folder}\' не существует')
                    print('*' * 51)
                    break
    elif choice == '3':
        print(f'{"*" * 18} КОПИРОВАНИЕ {"*" * 18} ')
        while True:
            choise = int(input('копировать папку - укажите \'1\', копировать файл - - укажите \'2\': '))
            if choise == 1:
                print(f'{"*" * 18} КОПИРОВАНИЕ ПАПКИ {"*" * 18} ')
                name_folder = input('укажите название папки для копирования: ')
                if os.path.exists(name_folder):
                    name_folder_new = input('укажите название новой папки: ')
                    shutil.copytree(name_folder, name_folder_new)
                    print(f'папка \'{name_folder}\' скопирована в \'{name_folder_new}\'')
                    print('*' * 51)
                    break
                else:
                    print(f'папка \'{name_folder}\' не существует. нечего копировать...')
            if choise == 2:
                print(f'{"*" * 18} КОПИРОВАНИЕ ФАЙЛА {"*" * 18} ')
                name_folder = input('укажите название файла для копирования: ')
                if os.path.exists(name_folder):
                    name_folder_new = input('укажите название нового файла: ')
                    shutil.copy(name_folder, name_folder_new)
                    print(f'файл \'{name_folder}\' скопирован в \'{name_folder_new}\'')
                    print('*' * 51)
                    break
                else:
                    print(f'файл \'{name_folder}\' не существует. нечего копировать...')
            else:
                print('неверный выбор')
    elif choice == '4':
        path = '.'
        rez = sorted(os.listdir())
        print(f'{"*" * 18} ФАЙЛЫ И ПАПКИ {"*" * 18} ')
        for n, item in enumerate(rez):
            print(n + 1, item)
        print('*' * 51)
    elif choice == '5':
        print(f'{"*" * 18} СПИСОК ПАПОК {"*" * 18} ')
        for counter in os.listdir():
            if os.path.isdir(counter):
                print(counter)
        print('*' * 51)
    elif choice == '6':
        print(f'{"*" * 18} СПИСОК ФАЙЛОВ {"*" * 18} ')
        for counter in os.listdir():
            if os.path.isfile(os.path.join(counter)):
                print(counter)
        print('*' * 51)
    elif choice == '7':
        print(f'Операционная система: {sys.platform}')
        print(f'Каталог установки Python: {sys.exec_prefix}')
        print(f'Путь к интерпретатору Python: {sys.executable}')
        print(f'Версия python: {sys.version}')
    elif choice == '8':
        print(f'{"*" * 18} СОЗДАТЕЛЬ ПРОГРАММЫ {"*" * 18} ')
        print(f'Создатель программы: {sys.copyright}')
        print('*' * 51)
    elif choice == '9':
        print(f'{"*" * 18} ВИКТОРИНА {"*" * 18} ')
        from famous_persons import get_person_and_question

        rounds = int(input('Сколько раз вы хотите играть?: '))

        for i in range(rounds):
            get_person_and_question()
        print('Пока!')
        print('*' * 51)
    elif choice == '10':
        print(f'{"*" * 18} КОШЕЛЕК {"*" * 18} ')
        from bank import banks
        banks()
    elif choice == '11':
        print(f'Текущий рабочий каталог {os.getcwd()}')
        new_path = input('Укажите новый рабочий каталог:')
        try:
            os.chdir(new_path)
            print(f'Текущий рабочий каталог {os.getcwd()}')
            print('*' * 51)
        except:
            print('*' * 51)
            print('неверный путь')
            print('-' * 51)
            print(sys.exc_info())
            print('-' * 51)
        finally:
            os.chdir(os.getcwd())
            print('текущий каталог', os.getcwd())
            print('*' * 51)
    elif choice == '12':
        print(f'{"*" * 18} ЧЕРЕПАШКА {"*" * 18} ')
        from tortila import my_turtle
        my_turtle()
    elif choice == '13':
        break

    else:
        print('Неверный пункт меню')