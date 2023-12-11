import ctypes
import os
from os import listdir, getcwd
from os.path import join, isfile

import win32com.client


def get_file_path(file_name, err_msg):
    curr_dir = getcwd()
    files = [f for f in listdir(curr_dir) if isfile(join(curr_dir, f))]
    for file in files:
        if file == file_name:
            return os.path.abspath(file)
    ctypes.windll.user32.MessageBoxW(0, err_msg, u"Ошибка", 0)
    return None


def create_shortcut(target_path, icon_path):
    appdata_folder = os.getenv('APPDATA')
    startup_folder = join(appdata_folder, 'Microsoft/Windows/Start Menu/Programs/Startup')
    lnk_path = join(startup_folder, 'JP Keyboard Layout Switcher.lnk')

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(lnk_path)
    shortcut.Targetpath = target_path
    shortcut.IconLocation = icon_path
    shortcut.WorkingDirectory = getcwd()
    shortcut.WindowStyle = 7
    shortcut.save()


def main():
    target_path = get_file_path('JP Keyboard Layout Switcher.exe', err_msg=u'В текущей папке нет файла приложения "app.exe"')
    if target_path is None:
        return
    icon_path = get_file_path('logo.ico', err_msg=u'В текущей папке нет файла иконки "logo.ico"')
    if icon_path is None:
        return
    create_shortcut(target_path, icon_path)


if __name__ == '__main__':
    main()
