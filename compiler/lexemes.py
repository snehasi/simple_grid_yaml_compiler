import yaml

def get_repo_list(site_level_configuration_file):
    with open(site_level_configuration_file, 'r') as stream:
        try:
            input_config_file = yaml.load(stream)
            url_list = []
            for each in input_config_file['lightweight_components']:
                url_list.append(each['repository_url'])
            
            return url_list

        except yaml.YAMLError as exc:
            print(exc)
            return []

def include_files(path):
    pass