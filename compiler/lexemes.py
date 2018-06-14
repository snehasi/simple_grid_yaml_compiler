import yaml

def get_repo_list(site_level_configuration_file):
    try:
        input_config_file = yaml.load(site_level_configuration_file)
        url_list = []
        for each in input_config_file['lightweight_components']:
            url_list.append(each['repository_url'])
            
        return url_list

    except yaml.YAMLError as exc:
        print(exc)
        return []

def include_files(path):
    pass