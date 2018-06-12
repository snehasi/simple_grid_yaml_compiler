import yaml, urllib2

def add_include_statements_for_default_files(list_default, config_file):
    
    with open(config_file, 'r') as stream:
        try:
            input_config_file = yaml.load(stream)
            input_config_file['include'] = list_default
            
            return input_config_file

        except yaml.YAMLError as exc:
            print(exc)
            return None

def add_included_files(augmented_yaml_file):

    for each_url in augmented_yaml_file['include']:
        new_url = each_url.replace("https://github.com/", "https://raw.githubusercontent.com/")

        data = urllib2.urlopen(new_url + "/master/default-data.yaml")
        augmented_yaml_file.update(yaml.load(data))

    augmented_yaml_file.pop('include')
    return augmented_yaml_file
        