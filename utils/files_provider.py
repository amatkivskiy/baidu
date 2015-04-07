from string import Template

__author__ = 'maa'

templates_folder = 'file_templates_folder\\'


def create_and_full_fill_file(template_file_name, destination_file_path, kwargs):
    template_file = open(template_file_name, 'r')
    file_content = template_file.read()
    template_file.close()

    template = Template(file_content)

    final_content = template.substitute(kwargs)

    final_file = open(destination_file_path, 'w')
    final_file.write(final_content)
    final_file.close()
