# FEATURES
## JP Keyboard Layout Switcher.exe
Creates a tray icon when clicked to enable/disable Japanese keyboard layout

Keyboard layout status is displayed by flag color

green - enable

red - disable
## Run on startup.exe
Creates a shortcut in the startup folder to run when windows starts

Default: C:\Users\[User]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
## Switcher.exe
Enable/disable JP keyboard layout without tray icon

You can configure the launch of Switcher.exe by hotkey

# HOW TO BUILD
## Run powershell in root folder and execute
```cmd
# Create .exe
pyinstaller --noconfirm --onefile --windowed --icon `
"C:/Projects/PET/JPKeyboardLayoutSwitcher/img/logo.ico" `
"C:/Projects/PET/JPKeyboardLayoutSwitcher/JP Keyboard Layout Switcher.py"

pyinstaller --noconfirm --onefile --windowed --icon `
"C:/Projects/PET/JPKeyboardLayoutSwitcher/img/logo.ico" `
"C:/Projects/PET/JPKeyboardLayoutSwitcher/Run on startup.py"

pyinstaller --noconfirm --onefile --windowed --icon `
"C:/Projects/PET/JPKeyboardLayoutSwitcher/img/logo.ico" `
"C:/Projects/PET/JPKeyboardLayoutSwitcher/Switcher.py"

# Move to release folder 
mkdir release
mv "dist/JP Keyboard Layout Switcher.exe" "release/JP Keyboard Layout Switcher.exe" 
mv "dist/Run on startup.exe" "release/Run on startup.exe" 
mv "dist/Switcher.exe" "release/Switcher.exe"
cp -r img release/

# Clear garbage
rm "JP Keyboard Layout Switcher.spec"
rm "Run on startup.spec"
rm "Switcher.spec"
rm -r -fo build
rm -r -fo dist

```