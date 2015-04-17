from utils.adb import Adb
from utils.files_provider import create_and_full_fill_file
from utils.msbuilder import MsBuilder
from utils.nuget import NuGet
from utils.util import create_or_clean_folder, find_open_port
from utils.xamarin_component import XamComponent
from utils.util import get_current_ip
from utils.touch_server import run
import ast

__author__ = 'maa'


def clean(config, params):
    check_if_all_params_specified(params, 'directory')
    directory = get_param_value('directory', params, config)

    print('Called clean_directory for ' + directory + '.')
    create_or_clean_folder(directory)

    pass

def restore_nuget(config, params):
    check_if_all_params_specified(params, 'solution', 'nuget_exe')
    nuget_path = get_param_value('nuget_exe', params, config)
    sln = get_param_value('solution', params, config)

    print('Nuget.exe path: ' + nuget_path)
    print('Restoring nuget packages: ' + sln)

    nuGet = NuGet(nuget_path)
    nuGet.restore_nuget_packages(sln)

def fulfill_file_template(config, params):
    check_if_all_params_specified(params, 'template', 'destination', 'ip', 'port', 'is_automated', 'is_remote', 'format')

    template_file = get_param_value('template', params, config)
    destination = get_param_value('destination', params, config)
    ip = get_param_value('ip', params, config)
    port = get_param_value('port', params, config)
    is_automated = get_param_value('is_automated', params, config)
    is_remote = get_param_value('is_remote', params, config)
    format = get_param_value('format', params, config)


    # TODO: Add ip check due to that it could be closed

    kwargs = {'is_automated': is_automated.lower(), 'is_remote': is_remote.lower(), 'ip': ip, 'port': port,
              'format': format}
    create_and_full_fill_file(template_file, destination, kwargs)


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


def run_tests(config, params):
    t_server_exe = config['touch_server_exe']

    activity = config['main_test_activity_name']
    logfile = config['test_results_file']

    run(touch_server_exe_path=t_server_exe, ip=ip, port=open_port, auto_exit=True, activity=activity, log_file=logfile)

    pass


def is_param_in_config(param, config):
    return param in config


def check_if_all_params_specified(params, *args):
    for arg in args:
        result = False
        for param in params:
            result = arg in param.keys() or result

        if not result:
            raise ValueError('Not all mandatory params for task specified. Params required: ' + str(arg))


def get_param_value(param_name, params, config):
        for param in params:
            if param_name in param.keys():
                param_value = param[param_name]

                if is_param_in_config(param_value, config):
                    param_value = config[param_value]
                else:
                    param_value = str(param_value).replace('\'', '')

                return  param_value





dictionary = {'clean_directory': clean,
              'restore_nuget_packages': restore_nuget,
              'restore_xam_components': restore_xam_comp,
              'msbuild_build_project': run_ms_build,
              'grab_logcat_results': grab_adb_logcat_results,
              'run_android_nunit_tests': run_tests,
              'fulfill_file_template': fulfill_file_template
              }

