from utils.adb import Adb
from utils.msbuilder import MsBuilder
from utils.nuget import NuGet
from utils.util import create_or_clean_folder
from utils.xamarin_component import XamComponent

__author__ = 'maa'


def clean(config, params):
    directory = config[params[0]]
    print('Called clean_directory for \'' + directory + '\'.')
    create_or_clean_folder(directory)

    pass


def restore_nuget(config, params):
    sln = config[params[0]]
    nuget_path = config['nuget']

    print('Nuget.exe path: ' + nuget_path)
    print('Restoring nuget packages: ' + sln)

    nuGet = NuGet(nuget_path)
    nuGet.restore_nuget_packages(sln)


def restore_xam_comp(config, params):
    sln = config[params[0]]
    xam_component_path = config['xamarin_component']

    print('xamarin-component.exe path: ' + xam_component_path)
    print('Restoring nuget packages: ' + sln)

    xam = XamComponent(xam_component_path)
    xam.restore_components(sln)

def run_ms_build(config, params):
    csproj = config[params[0]]
    targets = config[params[1]]
    configuration = config[params[2]]

    print('Building : ' + csproj)
    print('Targets : ' + str(targets))
    print('Configuration: ' + configuration)

    ms = MsBuilder(r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe')

    arg2 = ['Configuration=' + configuration]

    ms.build_with_params(csproj, targets=targets, properties=arg2)


def grab_adb_logcat_results(config, params):
    results_file = config[params[0]]

    print('Grabbing results from logcat to file : ' + results_file)

    adb = Adb()
    adb.grab_results(results_file)

dictionary = {'clean_directory': clean,
              'restore_nuget_packages': restore_nuget,
              'restore_xam_components': restore_xam_comp,
              'msbuild_build_project': run_ms_build,
              'grab_logcat_results' : grab_adb_logcat_results
              }




