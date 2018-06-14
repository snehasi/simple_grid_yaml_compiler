import yaml, re

def get_repo_list(site_level_configuration_file):
    try:
        input_config_file = yaml.load(site_level_configuration_file)
        url_list = []
        for each in input_config_file['lightweight_components']:
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', each['repository_url'])
            if not(urls == None):
                url_list.append(each['repository_url'])
            
        return url_list

    except yaml.YAMLError as exc:
        print(exc)
        return []

def include_files(path):
    pass