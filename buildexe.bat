DEL /q .\build\*
DEL /q .\dist\*
RD /S /Q .\build
RD /S /Q .\dist
pip install pyinstaller
@REM pyinstaller -w ./ImageTools.py --noconfirm --add-data "./Readme.html;./"
start cmd /c "pyinstaller -w ./ImageTools.py --noconfirm && copy .\Readme.html .\dist\ImageTools\ && copy .\version.md .\dist\ImageTools\ && compil32 /cc ./ImageTools.iss"
@REM start cmd /c "pyinstaller -w --noconfirm ./subapps/PQtools2Code.py && compil32 /cc ./subapps/PQtools2Code.iss"
@REM start cmd /c "pyinstaller -w --noconfirm ./subapps/ShakeTestTool.py && compil32 /cc ./subapps/ShakeTestTool.iss"
@REM start cmd /c "pyinstaller -w --noconfirm ./subapps/FocusDepthTool.py && compil32 /cc ./subapps/FocusDepthTool.iss"
@REM start cmd /c "pyinstaller -w --noconfirm ./subapps/VideoCompare.py && compil32 /cc ./subapps/VideoCompare.iss"