rm -r build
rm -r dist
pyinstaller -w ./ImageTools.py --noconfirm
copy .\Readme.md .\dist\ImageTools\
