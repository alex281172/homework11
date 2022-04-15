import os
import shutil
import sys
import shutil
import turtle
from functioms_filemanager import *
from tortila import my_turtle




with open('history_oder.txt', 'w') as f:
    f.write('')

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. Черепашка')
    print('13. сохранить содержимое рабочей директории в файл')
    print('14. выход')



    choice = input('Выберите пункт меню Консольного файлового менеджера -> ')
    if choice == '1':
        create_folder()

    elif choice == '2':
        delete_file_folder()

    elif choice == '3':
        copy_file_folder()

    elif choice == '4':
        list_working_dir()

    elif choice == '5':
        list_folders()

    elif choice == '6':
        list_files()

    elif choice == '7':
        print_info()

    elif choice == '8':
        print_author()

    elif choice == '9':
        play_victory()

    elif choice == '10':
        run_bank()

    elif choice == '11':
        change_workig_dir()

    elif choice == '12':
        run_turtle()

    elif choice == '13':
        save_info_file()

    elif choice == '14':
        break
    else:
        print('Неверный выбор меню')