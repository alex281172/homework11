import os
import shutil
from decorate import add_separators
import sys
from tortila import my_turtle


if '__name__' != '__main__':

    def author_info():
        return 'Aleksey Savotchenko'

    def separator(count=51):
        return '*' * count
    def separator1(count=51):
        return '-' * count

    @add_separators
    def copy_file_folder():
        print(f'{"*" * 18} КОПИРОВАНИЕ ПАПКИ/ФАЙЛА {"*" * 18} ')
        name_item = input('укажите название папки или файла для копирования: ')
        if os.path.exists(name_item):
            name_item_new = input('укажите название новой папки или файла: ')
            shutil.copytree(name_item, name_item_new) if os.path.isdir(name_item) else shutil.copy(name_item, name_item_new)
            print(f'\'{name_item}\' скопирован в \'{name_item_new}\'')
        else:
            print(f'\'{name_item}\' не существует. нечего копировать...')


    @add_separators
    def delete_file_folder():
        print(f'{"*" * 18} УДАЛЕНИЕ ПАПКИ/ФАЙЛА {"*" * 18} ')
        name_item = input('укажите название папки или файла для удаления: ')
        if os.path.exists(name_item):
            os.rmdir(f'{os.getcwd()}\{name_item}') if os.path.isdir(name_item) else os.remove(
                f'{os.getcwd()}\{name_item}')
            print(f'\'{name_item}\' удален')
        else:
            print(f'\'{name_item}\' не существует. нечего удалять...')



    @add_separators
    def list_working_dir():
        print(f'{"*" * 18} ФАЙЛЫ И ПАПКИ {"*" * 18} ')
        for n, item in enumerate(os.listdir()):
            print(n + 1, item)
        print(separator())

    @add_separators
    def list_folders():
        print(f'{"*" * 18} СПИСОК ПАПОК {"*" * 18} ')
        for name_item in os.listdir():
            if os.path.isdir(name_item):
                print(name_item)
        print(separator())

    @add_separators
    def list_files():
        print(f'{"*" * 18} СПИСОК ФАЙЛОВ {"*" * 18} ')
        for name_item in os.listdir():
            if os.path.isfile(name_item):
                print(name_item)
        print(separator())

    @add_separators
    def print_info():
        print(f'Операционная система: {sys.platform}')
        print(f'Каталог установки Python: {sys.exec_prefix}')
        print(f'Путь к интерпретатору Python: {sys.executable}')
        print(f'Версия python: {sys.version}')

    @add_separators
    def print_author():
        print(f'{"*" * 18} СОЗДАТЕЛЬ ПРОГРАММЫ {"*" * 18} ')
        print(f'Создатель программы \'Консольный файловый менеджер\': {author_info()}')
        print(separator())
        print(separator())
        print(f'Copyright: {sys.copyright}')
        print(separator())

    @add_separators
    def play_victory():
        print(f'{"*" * 18} ВИКТОРИНА {"*" * 18} ')

        while True:
            try:
                from famous_persons import get_person_and_question
                rounds = int(input('Сколько раз вы хотите играть?: '))
                for i in range(rounds):
                    get_person_and_question()
                break
            except ValueError:
                print('введите число')
        print('Пока!')
        print(separator())

    @add_separators
    def run_bank():
        print(f'{"*" * 18} КОШЕЛЕК {"*" * 18} ')
        from bank import banks
        banks()

    @add_separators
    def change_workig_dir():
        print(f'Текущий рабочий каталог {os.getcwd()}')
        new_path = input('Укажите новый рабочий каталог:')
        try:
            os.chdir(new_path)
            print(f'Текущий рабочий каталог {os.getcwd()}')
            print(separator())
        except:
            print(separator())
            print('неверный путь')
            print(separator1())
            print(sys.exc_info())
            print(separator1())
        finally:
            os.chdir(os.getcwd())
            print('текущий каталог', os.getcwd())
            print(separator())

    @add_separators
    def run_turtle():
        print(f'{"*" * 18} ЧЕРЕПАШКА {"*" * 18} ')
        my_turtle()

    @add_separators
    def save_info_file():
        print(f'{"*" * 5} выгрузка в ФАЙЛ \'list_dirs_files.txt\' списка  {"*" * 5} ')
        with open('list_dirs_files.txt', 'w') as f:
            f.write('')
        with open('list_dirs_files.txt', 'a', encoding='utf-8') as f:
            f.write('dirs: ')
            for name_item in os.listdir():
                if os.path.isdir(name_item):
                    f.write(name_item)
                    f.write(', ')
            f.write('\n')
            f.write('files: ')
            for name_item in os.listdir():
                if os.path.isfile(name_item):
                    f.write(name_item)
                    f.write(', ')
        with open('list_dirs_files.txt', 'r', encoding='utf-8') as f:
           list_dirs_files = f.read()
        print(list_dirs_files)

    @add_separators
    def create_folder():
        print(f'{"*" * 18} СОЗДАНИЕ ПАПКИ {"*" * 18} ')
        while True:
            name_folder = input('укажите название папки для создания: ')
            if not os.path.exists(name_folder):
                os.mkdir(f'{name_folder}')
                print(f'папка \'{name_folder}\' создана')
                print(separator())
                break
            else:
                print(f'папка \'{name_folder}\' существует')
                print(separator())
            break




