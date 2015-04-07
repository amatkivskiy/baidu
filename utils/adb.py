from utils.util import run_command

__author__ = 'maa'

class Adb:
    def __init__(self, adb_path=None):
        if adb_path == None:
            self.adb = 'adb'
        else:
            self.adb = adb_path

    def install_apk(self, path_to_apk):
        params = [self.adb, 'install', '-r', path_to_apk]

        run_command(params)

    def grab_results(self, results_file):
        params = [self.adb, 'logcat', '-d']

        with open(results_file, 'w') as file:
            run_command(params, std_out=file)

        pass