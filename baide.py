import sys
import re
import yaml
from commands import dictionary

__author__ = 'maa'


def run_function(task_name, config, params):
    try:
        dictionary[task_name](config, params)
    except KeyError:
        print('No functions found for ' + task_name)
    pass

def split_task_name(task_name):
    start_index = task_name.index('(')
    return task_name[:start_index]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise EnvironmentError('Please provide config file for script.')

    stream = open(sys.argv[1], 'r')
    config = yaml.load(stream)

    p = re.compile('\((.*?)\)')

    for task in config['tasks']:
        params = p.findall(task)
        task_name = split_task_name(task)
        run_function(task_name, config, params)

    pass
