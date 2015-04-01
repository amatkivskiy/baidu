import os

from utils.util import run_command


__author__ = 'maa'


class NuGet:
    def __init__(self, nuGetExePath):
        self.nuGetExePath = nuGetExePath
        self._validate_nuget_exe()

    def run_nuget_exe_update(self, ignoreReturnCode=False):
        args = [self.nuGetExePath, 'update', '-Self']
        run_command(args, ignoreReturnCode)

    def restore_nuget_packages(self, slnPath, ignoreReturnCode=False):
        args = [self.nuGetExePath, 'restore', '-NoCache', slnPath]
        run_command(args, ignoreReturnCode)

    def _validate_nuget_exe(self):
        if not os.path.isfile(self.nuGetExePath):
            raise Exception('NuGet.exe not found. path = ' + self.nuGetExePath)
        pass