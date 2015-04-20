import os
import datetime

from utils.util import run_command


__author__ = 'maa'

class MsBuilder:
    def __init__(self, msbuild):
        if msbuild == None:
            self.msbuild = r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe"
        else:
            self.msbuild = msbuild

    def build_with_params(self, csprojPath, targets, properties):
        if not os.path.isfile(self.msbuild):
            raise Exception('MsBuild.exe not found. path = ' + self.msbuild)

        start = datetime.datetime.now()
        print('STARTED BUILD - ' + start.strftime('%Y-%m-%d %H:%M:%S'))

        params = [self.msbuild, csprojPath]

        params.append('/t:' + ';'.join(targets))
        params.append('/p:' + ';'.join(properties))

        return run_command(params)

    def build(self, csprojPath, args):
        if not os.path.isfile(self.msbuild):
            raise Exception('MsBuild.exe not found. path = ' + self.msbuild)

        start = datetime.datetime.now()
        print('STARTED BUILD - ' + start.strftime('%Y-%m-%d %H:%M:%S'))

        params = [self.msbuild, csprojPath] + list(args)

        return run_command(params)

    def get_files_from_project_bin_folder(self, csproj, configuration, do_return_full_paths=False):
        name = os.path.dirname(os.path.realpath(csproj))
        bin_config_path = os.path.join(name, 'bin', configuration)

        files = os.listdir(bin_config_path)

        if not do_return_full_paths:
            return files

        files_full_path = list()

        for file in files:
            files_full_path.append(os.path.join(bin_config_path, file))

        return files_full_path
