DEL /q .\build\*
DEL /q .\dist\*
RD /S /Q .\build
RD /S /Q .\dist
start cmd /c "pyinstaller -w ./ImageTools.py --noconfirm && copy .\Readme.html .\dist\ImageTools\ && compil32 /cc ./ImageTools.iss"
start cmd /c "pyinstaller -w --noconfirm ./subapps/PQtools2Code.py && compil32 /cc ./subapps/PQtools2Code.iss"
start cmd /c "pyinstaller -w --noconfirm ./subapps/ShakeTestTool.py && compil32 /cc ./subapps/ShakeTestTool.iss"
start cmd /c "pyinstaller -w --noconfirm ./subapps/FocusDepthTool.py && compil32 /cc ./subapps/FocusDepthTool.iss"
start cmd /c "pyinstaller -w --noconfirm ./subapps/VideoCompare.py && compil32 /cc ./subapps/VideoCompare.iss"