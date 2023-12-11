import re
import subprocess
import pystray
import PIL.Image

ACTIVE_LOGO = PIL.Image.open('img/active.png')
INACTIVE_LOGO = PIL.Image.open('img/inactive.png')
GET_LOCALES_CMD = '$List = Get-WinUserLanguageList\n$List'
INSTALL_CMD = '$List = Get-WinUserLanguageList\n$List.Add("ja-JP")\nSet-WinUserLanguageList $List -Force'
UNINSTALL_CMD = '$List = Get-WinUserLanguageList\n$remove = $List | where LanguageTag -eq "ja"\n$List.Remove($remove)\nSet-WinUserLanguageList $List -Force'
JAPANESE_LANGUAGE_TAG = 'ja'


class App:
    def __init__(self):
        self.status = JAPANESE_LANGUAGE_TAG in self.get_langs()
        self.app = None

    def run(self):
        self.app = self.get_app()
        self.app.run()

    def get_app(self):
        return pystray.Icon('JP Switcher', ACTIVE_LOGO if self.status else INACTIVE_LOGO, menu=pystray.Menu(
            pystray.MenuItem(text='Переключить', action=self.on_clicked, default=True),
            pystray.MenuItem(text='Выйти', action=self.app_exit)
        ))

    def on_clicked(self, icon):
        icon.icon = INACTIVE_LOGO if self.status else ACTIVE_LOGO
        self.switch()
        self.status = not self.status

    @staticmethod
    def app_exit(icon):
        icon.stop()

    @staticmethod
    def exec_cmd(cmd):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        return subprocess.Popen(["powershell", cmd], startupinfo=si, stdout=subprocess.PIPE).communicate()

    def get_langs(self):
        raw_out, _ = self.exec_cmd(GET_LOCALES_CMD)
        return re.findall(r'LanguageTag {5}: (.*)\r', raw_out.decode('ascii', 'ignore'))

    def switch(self):
        if self.status:
            self.exec_cmd(UNINSTALL_CMD)
        else:
            self.exec_cmd(INSTALL_CMD)


if __name__ == '__main__':
    app = App()
    app.run()
