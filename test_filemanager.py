import os
import shutil

from functioms_filemanager import *

assert author_info() == 'Aleksey Savotchenko'

def test_autor_info():
    assert author_info() == 'Aleksey Savotchenko'

def test_mkdir():
    if os.path.exists('folder_test'):
        os.rmdir('folder_test')
    os.mkdir('folder_test')
    assert 'folder_test' in os.listdir()

def test_shutil_tree():
    if os.path.exists('folder_test'):
        os.rmdir('folder_test')
    if os.path.exists('folder_test_new'):
        os.rmdir('folder_test_new')
    os.mkdir('folder_test')
    shutil.copytree('folder_test', 'folder_test_new')
    assert 'folder_test_new' in os.listdir()


