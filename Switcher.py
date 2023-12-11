import re
import subprocess

GET_LOCALES_CMD = '$List = Get-WinUserLanguageList\n$List'
INSTALL_CMD = '$List = Get-WinUserLanguageList\n$List.Add("ja-JP")\nSet-WinUserLanguageList $List -Force'
UNINSTALL_CMD = '$List = Get-WinUserLanguageList\n$remove = $List | where LanguageTag -eq "ja"\n$List.Remove($remove)\nSet-WinUserLanguageList $List -Force'
JAPANESE_LANGUAGE_TAG = 'ja'


def exec_cmd(cmd):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return subprocess.Popen(["powershell", cmd], startupinfo=si, stdout=subprocess.PIPE).communicate()


def get_langs():
    raw_out, _ = exec_cmd(GET_LOCALES_CMD)
    return re.findall(r'LanguageTag {5}: (.*)\r', raw_out.decode('ascii', 'ignore'))


def switch(status):
    if status:
        exec_cmd(UNINSTALL_CMD)
    else:
        exec_cmd(INSTALL_CMD)


def main():
    status = JAPANESE_LANGUAGE_TAG in get_langs()
    switch(status)


if __name__ == '__main__':
    main()
