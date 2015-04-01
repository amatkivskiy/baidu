import os
import socket
import subprocess
import shutil

__author__ = 'maa'


def run_command(args, ignoreReturnCode=False, is_shell=False):
    print('=' * 20)
    print('Printing command details')

    print('*' * 20)
    for arg in args:
        print("\"" + arg + "\"")

    print('*' * 20)
    print('=' * 20)

    returnCode = subprocess.call(args, shell=is_shell)

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


def check_if_port_is_open(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((ip, port))
    sock.close()

    return result != 0

def find_open_port(ip, starting_port, max_port):
    port = starting_port

    while port <= max_port:
        if check_if_port_is_open(ip, port):
            return port
        else:
            port += 1

    raise ConnectionError('Open port was not found between ' + str(starting_port) + ' and ' + str(max_port))