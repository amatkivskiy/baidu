import os
import shutil
from utils.adb import Adb
from utils.files_provider import create_and_full_fill_file
from utils.msbuilder import MsBuilder
from utils.nuget import NuGet
from utils.util import create_or_clean_folder, clean_xamarin_cache
from utils.xamarin_component import XamComponent
from utils.touch_server import run

__author__ = 'maa'


def clean_directory(config, params):
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
    check_if_all_params_specified(params, 'template', 'destination', 'ip', 'port', 'is_automated', 'is_remote',
                                  'format')

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
    check_if_all_params_specified(params, 'solution', 'xam_exe')
    xam_component_path = get_param_value('xam_exe', params, config)
    sln = get_param_value('solution', params, config)

    print('xamarin-component.exe path: ' + xam_component_path)
    print('Restoring nuget packages: ' + sln)

    xam = XamComponent(xam_component_path)
    xam.restore_components(sln)


def run_ms_build(config, params):
    check_if_all_params_specified(params, 'project', 'targets', 'configuration')
    csproj = get_param_value('project', params, config)
    targets = get_param_value('targets', params, config)
    configuration = get_param_value('configuration', params, config)

    print('Building : ' + csproj)
    print('Targets : ' + str(targets))
    print('Configuration: ' + configuration)

    ms = MsBuilder(r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe')

    arg2 = ['Configuration=' + configuration]

    ms.build_with_params(csproj, targets=targets.split(','), properties=arg2)


def run_tests(config, params):
    check_if_all_params_specified(params, 'touch_server', 'activity', 'results_file', 'ip', 'port')

    activity = get_param_value('activity', params, config)
    logfile = get_param_value('results_file', params, config)
    ip = get_param_value('ip', params, config)
    port = get_param_value('port', params, config)
    t_server_exe = get_param_value('touch_server', params, config)

    run(touch_server_exe_path=t_server_exe, ip=ip, port=port, auto_exit=True, activity=activity, log_file=logfile)

    pass


def grab_adb_logcat_results(config, params):
    check_if_all_params_specified(params, 'log_file')
    results_file = get_param_value('log_file', params, config)

    print('Grabbing results from logcat to file : ' + results_file)

    adb = Adb()
    adb.grab_results(results_file)

def copy_artifacts(config, params):
    check_if_all_params_specified(params, 'from', 'to')

    from_file = get_param_value('from', params, config)
    to_file = get_param_value('to', params, config)

    print('Coping file {0} to {1}'.format(from_file, to_file))

    shutil.copyfile(from_file, to_file)

def manage_nuget_sources(config, params):
    check_if_all_params_specified(params, 'nuget_config_file', 'custom_source_directory', 'custom_source_name', 'template_file')

    config_file = get_param_value('nuget_config_file', params, config)
    directory = get_param_value('custom_source_directory', params, config)
    name = get_param_value('custom_source_name', params, config)
    template_file = get_param_value('template_file', params, config)

    print('Config file : {0}, directory : {1}, name : {2}'.format(config_file, directory, name))

    os.rename(config_file, config_file + '.orig')

    kwargs = {'source_name': name, 'source_directory': directory}
    create_and_full_fill_file(template_file, config_file, kwargs)

def restore_changed_nuget_config(config, params):
    check_if_all_params_specified(params, 'nuget_config_file')

    config_file = get_param_value('nuget_config_file', params, config)

    print('Config file : {0}.'.format(config_file))

    os.remove(config_file)
    os.rename(config_file + '.orig', config_file)

    pass

def clear_xamarin_cache(config, params):
    clean_xamarin_cache()
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

            if type(param_value) is str and '$(' in param_value:
                param_value = get_param_value_with_variable(config, param_value)

            if type(param_value) is str and '%(' in param_value:
                param_value = get_param_value_from_env(param_value)

            param_value = str(param_value).replace('\'', '')

            return param_value


def get_param_value_from_env(param_value):
    percent_index = param_value.find('%')
    parenthesis_open = str(param_value).find('(', percent_index)
    parenthesis_close = str(param_value).find(')', parenthesis_open)

    extracted_param_name = param_value[parenthesis_open + 1:parenthesis_close]

    result = os.environ.get(extracted_param_name)
    if result is None:
        raise ValueError('There is no "{0}" environment variable.'.format(extracted_param_name))

    return str(param_value).replace('%(' + extracted_param_name + ')', result)


def get_param_value_with_variable(config, param_value):
    dollar_index = param_value.find('$')
    parenthesis_open = str(param_value).find('(', dollar_index)
    parenthesis_close = str(param_value).find(')', parenthesis_open)

    extracted_param_name = param_value[parenthesis_open + 1:parenthesis_close]

    if is_param_in_config(extracted_param_name, config):
        variable_value = config[extracted_param_name]

        return str(param_value).replace('$(' + extracted_param_name + ')', variable_value)
    else:
        raise ValueError('Can\'t find variable {0} in config root. Have you specified it?'.format(extracted_param_name))


dictionary = {'clean_directory': clean_directory,
              'restore_nuget_packages': restore_nuget,
              'restore_xam_components': restore_xam_comp,
              'msbuild_build_project': run_ms_build,
              'grab_logcat_results': grab_adb_logcat_results,
              'run_android_nunit_tests': run_tests,
              'fulfill_file_template': fulfill_file_template,
              'copy_artifacts': copy_artifacts,
              'clear_xamarin_cache': clear_xamarin_cache,
              'manage_nuget_sources': manage_nuget_sources,
              'restore_changed_nuget_config': restore_changed_nuget_config,
              }

