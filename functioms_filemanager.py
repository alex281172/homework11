import os
import shutil
if '__name__' != '__main__':

    def author_info():
        return 'Aleksey Savotchenko'

    def separator(count=51):
        return '*' * count
    def separator1(count=51):
        return '-' * count

    def save_info():
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



    def copy_file_folder():
        print(f'{"*" * 18} КОПИРОВАНИЕ ПАПКИ/ФАЙЛА {"*" * 18} ')
        name_item = input('укажите название папки или файла для копирования: ')
        if os.path.exists(name_item):
            name_item_new = input('укажите название новой папки или файла: ')
            if os.path.isdir(name_item):
                shutil.copytree(name_item, name_item_new)
            else:
                shutil.copy(name_item, name_item_new)
            print(f'\'{name_item}\' скопирован в \'{name_item_new}\'')
        else:
            print(f'\'{name_item}\' не существует. нечего копировать...')

    def delete_file_folder():
        print(f'{"*" * 18} УДАЛЕНИЕ ПАПКИ/ФАЙЛА {"*" * 18} ')
        name_item = input('укажите название папки или файла для удаления: ')
        if os.path.exists(name_item):
            if os.path.isdir(name_item):
                os.rmdir(f'{os.getcwd()}\{name_item}')
            else:
                os.remove(f'{os.getcwd()}\{name_item}')
            print(f'\'{name_item}\' удален')
        else:
            print(f'\'{name_item}\' не существует. нечего удалять...')





