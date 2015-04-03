from utils.nuget import NuGet
from utils.util import create_or_clean_folder
from utils.xamarin_component import XamComponent

__author__ = 'maa'


def clean_directory(config, params):
    directory = config[params[0]]
    print('Called clean_directory for \'' + directory + '\'.')
    create_or_clean_folder(directory)

    pass


def nuget_packages_restore(config, params):
    sln = config[params[0]]
    nuget_path = config['nuget']

    print('Nuget.exe path: ' + nuget_path)
    print('Restoring nuget packages: ' + sln)

    nuGet = NuGet(nuget_path)
    nuGet.restore_nuget_packages(sln)

def restore_xam_components(config, params):
    sln = config[params[0]]
    xam_component_path = config['xamarin_component']

    print('xamarin-component.exe path: ' + xam_component_path)
    print('Restoring nuget packages: ' + sln)

    xam = XamComponent(xam_component_path)
    xam.restore_components(sln)

dictionary = {'clean_directory': clean_directory,
              'restore_nuget_packages': nuget_packages_restore,
              'restore_xam_components': restore_xam_components
              }




