import os
import subprocess

__author__ = 'maa'

class NuGet:
    def __init__(self, nuGetExePath):
        self.nuGetExePath = nuGetExePath
        self.validateNuGetExe()

    def runNuGetExeUpdate(self, ignoreReturnCode=False):
        args = ['update', '-Self']
        self.runCommand(args, ignoreReturnCode)

    def restoreNuGetPackages(self, slnPath, ignoreReturnCode=False):
        args = ['restore', '-NoCache', slnPath]
        self.runCommand(args, ignoreReturnCode)

    def validateNuGetExe(self):
        if not os.path.isfile(self.nuGetExePath):
            raise Exception('NuGet.exe not found. path = ' + self.nuGetExePath)
        pass

    def runCommand(self, args, ignoreReturnCode=False):
        newArgs = [self.nuGetExePath]

        [newArgs.append(arg) for arg in args]

        print('=' * 20)
        print('Printing NuGet command details')
        print('NuGet.exe path : ' + self.nuGetExePath)

        print('*' * 20)
        for arg in args:
            print("\"" + arg + "\"")

        print('*' * 20)
        print('=' * 20)

        returnCode = subprocess.call(newArgs)

        if returnCode != 1:
            print('Successfully executed command')
        elif not ignoreReturnCode:
            raise Exception('Failed to executed command')

        pass