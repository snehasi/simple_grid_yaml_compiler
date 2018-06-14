import yaml

def check_yaml_syntax(final_yaml_file):
    try:
        yaml.load(yaml.dump(final_yaml_file))

        return final_yaml_file
    except yaml.YAMLError as exc:
        print(exc)
        return final_yaml_file
