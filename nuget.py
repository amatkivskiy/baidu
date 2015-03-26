import os

from util import run_command


__author__ = 'maa'


class NuGet:
    def __init__(self, nuGetExePath):
        self.nuGetExePath = nuGetExePath
        self._validateNuGetExe()

    def runNuGetExeUpdate(self, ignoreReturnCode=False):
        args = [self.nuGetExePath, 'update', '-Self']
        run_command(args, ignoreReturnCode)

    def restoreNuGetPackages(self, slnPath, ignoreReturnCode=False):
        args = [self.nuGetExePath, 'restore', '-NoCache', slnPath]
        run_command(args, ignoreReturnCode)

    def _validateNuGetExe(self):
        if not os.path.isfile(self.nuGetExePath):
            raise Exception('NuGet.exe not found. path = ' + self.nuGetExePath)
        pass

