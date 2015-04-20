import sys
import re

import yaml

from commands import dictionary


__author__ = 'maa'


def run_function(task_name, config, params):
    try:
        dictionary[task_name](config, params)
    except KeyError:
        print('No function found for ' + task_name)
    pass

def split_task_name(task_name):
    start_index = task_name.index('(')
    return task_name[:start_index]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise EnvironmentError('Please provide config file for script.')

    command = sys.argv[1]
    if 'doit' != command:
        print('Baide: I don\'t know what you mean :(')
        quit()

    stream = open(sys.argv[2], 'r')
    config = yaml.load(stream)

    p = re.compile('\((.*?)\)')

    for task in config['tasks']:
        task_name = list(task.keys())[0]

        params = task[task_name]
        run_function(task_name, config, params)
    pass
