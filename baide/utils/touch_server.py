from utils.util import run_command

__author__ = 'maa'


def run(touch_server_exe_path, ip=None, port=None, auto_exit=False, activity=None, log_file=None, log_path=None,
        adb_path=None):
    params = list()
    params.append(touch_server_exe_path)

    if ip:
        params.append('--ip=' + ip)

    if port:
        params.append('--port=' + str(port))

    if auto_exit:
        params.append('--autoexit')

    if activity:
        params.append('--activity=' + activity)

    if log_file:
        params.append('--logfile=' + log_file)

    if log_path:
        params.append('--logpath=' + log_path)

    if adb_path:
        params.append('--adbPath=' + adb_path)

    run_command(params, is_shell=True)


