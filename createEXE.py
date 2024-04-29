import PyInstaller.__main__
import os

name = "removeFirstPage"

if not os.path.exists(f"./dist/{name}.exe"):
    options = ['--onefile', 'main.py']
    PyInstaller.__main__.run(options)
    os.rename("./dist/main.exe", f"./dist/{name}.exe")
else:
    print("EXE already exists, delete it first!")

quit()
