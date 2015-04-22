SET script_directory=%~dp0
SET script_file=baidu.py

call python %script_directory%%script_file% %*
