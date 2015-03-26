import subprocess

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