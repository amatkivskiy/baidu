from string import Template

__author__ = 'maa'

templates_folder = 'file_templates_folder\\'


def create_and_full_fill_file(template_file_name, destination_file_path, file_name, kwargs):
    template_file = open(templates_folder + template_file_name, 'r')
    file_content = template_file.read()
    template_file.close()

    template = Template(file_content)

    final_content = template.substitute(kwargs)

    final_file = open(destination_file_path + '\\' + file_name, 'w')
    final_file.write(final_content)
    final_file.close()
