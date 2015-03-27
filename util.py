import os
import subprocess
import shutil

__author__ = 'maa'


def run_command(args, ignoreReturnCode=False):
    print('=' * 20)
    print('Printing command details')

    print('*' * 20)
    for arg in args:
        print("\"" + arg + "\"")

    print('*' * 20)
    print('=' * 20)

    returnCode = subprocess.call(args)

    if returnCode != 1:
        print('Successfully executed command')
    elif not ignoreReturnCode:
        raise Exception('Failed to executed command')

    pass


def create_or_clean_folder(folder_path):
    if not os.path.exists(folder_path):
        print('Creating folder : ' + folder_path)
        os.makedirs(folder_path)
    else:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
    pass