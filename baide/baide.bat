SET script_directory=%~dp0
SET script_file=baide.py

call python %script_directory%%script_file% %*
