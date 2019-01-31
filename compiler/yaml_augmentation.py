import re, copy
from compiler import runtime_variables
from ruamel.yaml.comments import CommentedSeq, CommentedMap


def add_include_statements(files_path_array, site_level_configuration_file):
        output = open('./.temp/site_level_configuration_file_unprocessed_includes', 'w')
        for file_name in files_path_array:
            try:
                output.write("include: '" + file_name + "'\n")
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


def split_component_config(input_data):
    components = input_data['lightweight_components']
    updated_components = CommentedSeq()
    ## deep copy
    for component in components:
        number_of_nodes = len(component['deploy'])

        for idx, val in enumerate(component['deploy']):
            temp_component = copy.deepcopy(component)
            temp_component['deploy'] = copy.deepcopy(component['deploy'][idx])
            updated_components.append(temp_component)

    components = updated_components
    input_data['lightweight_components'] = components
    return input_data


def add_component_ids(input_data):
    components = input_data['lightweight_components']
    number_of_components = len(components)
    for i in range(number_of_components):
        print i
        print input_data['lightweight_components'][i]
        input_data['lightweight_components'][i].setdefault('id', i)
    return input_data


