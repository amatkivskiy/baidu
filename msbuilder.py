import os
import subprocess
import datetime

__author__ = 'maa'

class MsBuilder:
    def __init__(self, msbuild):
        if msbuild == None:
            self.msbuild = r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe"
        else:
            self.msbuild = msbuild

    def build(self, csprojPath, *args):
        if not os.path.isfile(self.msbuild):
            raise Exception('MsBuild.exe not found. path = ' + self.msbuild)

        start = datetime.datetime.now()
        print('STARTED BUILD - ' + start.strftime('%Y-%m-%d %H:%M:%S'))

        self.printConfig(csprojPath, args)

        params = [self.msbuild, csprojPath] + list(args);

        returnCode = subprocess.call(params)
        if returnCode != 1:
            print('BUILD: SUCCEEDED', start)
        else:
            print('BUILD: FAILED', start)

        return returnCode != 1

    def printConfig(self, csprojPath, params):
        print('Printing MsBuild params:')
        print('=' * 20)

        print('Project path: ' + csprojPath)

        print('MSBuild.exe params : ')
        print('*' * 20)
        for param in params:
            print(param)

        print('*' * 20)
        print('=' * 20)