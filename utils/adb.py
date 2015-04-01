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
