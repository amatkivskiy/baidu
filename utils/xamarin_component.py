import os
import shutil

from utils.util import run_command


__author__ = 'maa'

class XamComponent:
    def __init__(self, xam_component_path):
        self.xam_component_path = xam_component_path
        
        self._validate_component_path()

    def install_component(self, xam_file_path):
        args = [self.xam_component_path, 'install', xam_file_path]

        run_command(args)

    def clean_xamarin_cache(self):
        path = os.getenv('LOCALAPPDATA') + r"\Xamarin\Cache"
        print('Deleting folder : ' + path)
        shutil.rmtree(path, True)

    def restore_components(self, solution_path):
        args = [self.xam_component_path, 'restore', solution_path]

        run_command(args)

    def _validate_component_path(self):
         if not os.path.isfile(self.xam_component_path):
            raise Exception('Xamarin component exe not found. path = ' + self.xam_component_path)
         pass