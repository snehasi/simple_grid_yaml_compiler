import yaml

def check_yaml_syntax(expanded_yaml_file):
    # try:
        expanded_yaml_file_temp = open(expanded_yaml_file.name, 'r')
        print("*******************")
        augmented_yaml = yaml.load(expanded_yaml_file_temp)
        print("Augmented Data is")
        print(augmented_yaml)
        with open("./.temp/augmented_yaml_file_final.yaml", 'w') as augmented_site_level_configuration_file:
            print yaml.dump(augmented_yaml, default_flow_style=False)
            print("*******************")
            return augmented_site_level_configuration_file
        expanded_yaml_file.close()
        return None
    # except yaml.YAMLError as exc:
    #     print(exc.message)
    #     return expanded_yaml_file
