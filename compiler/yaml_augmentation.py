import re
from compiler import runtime_variables


def add_include_statements_for_default_files(file_names_repository_default, site_level_configuration_file):
        output = open('./.temp/site_level_configuration_file_unprocessed_includes', 'w')
        for file_name_repository_default in file_names_repository_default:
            try:
                output.write("include: '" + file_name_repository_default + "'\n")
            except Exception as ex:
                print ex.message

        site_level_configuration_file.seek(0)
        output.writelines(l for l in site_level_configuration_file.readlines())
        output.close()
        return output


def expand_file_from_include_statements(augmented_yaml_file, yaml_file_to_be_expanded):
    f = open(yaml_file_to_be_expanded, 'r')
    for l in f.readlines():
        search_results = re.search('(include:.*)', l)
        if search_results is not None:
            include_string = search_results.group()
            file_path = include_string.split(':')[1].strip()
            if file_path.startswith("'") or file_path.startswith("\""):
                file_path = file_path[1: -1]
            expand_file_from_include_statements(augmented_yaml_file, file_path)
        else:
            augmented_yaml_file.write(l)
    augmented_yaml_file.write("\n")
    f.close()


def add_included_files(default_includes_yaml_file):
    expanded_yaml_file = open('./.temp/expanded_yaml_file.yaml', 'w')
    expand_file_from_include_statements(expanded_yaml_file, default_includes_yaml_file.name)
    expanded_yaml_file.close()
    return expanded_yaml_file