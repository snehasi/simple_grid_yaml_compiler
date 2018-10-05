import yaml


def find_component_data(data, meta_info):
    components = []
    for component in data['lightweight_components']:
        if component['name'] == meta_info['component']:
            components.append(component)

    return components


def lookup(data, key, parameter):
    value = None
    try:
        value = data[key][parameter]
    except Exception as ex:
        pass
    return value

def lookup_defaults(default_data, meta_info, parameter):
    default_value = None
    #try:
    default_value = default_data[meta_info['default_var_prefix'] + '_' + parameter]
    #except Exception as ex:
    #    print ex.message

    return default_value


def get_final_config_values_for_component(component, expected_params, defaults_for_expected_params, meta_info):
        final_component_data = {}
        print " No of expected params: " + str(len(expected_params))
        i=0
        for config_param in expected_params:
            value = None
            i=i+1
            print "  - Param " + str(i) + " :" +config_param
            if expected_params[config_param]['required']:
                print "     - required: True"
                value_defined_by_user = lookup(component, meta_info['primary_config_key'], config_param)
                if value_defined_by_user != None:
                    print "     - specified: True"
                    value = value_defined_by_user
                    print "     - user-defined-value: " + str(value)
                else:
                    print "     - specified: False"
                    #check use_default
                    if expected_params[config_param]['use_default']:
                        print "     - use-default: True"
                        default_value = lookup_defaults(defaults_for_expected_params, meta_info, config_param)
                        print "     - default-value: " + str(default_value)
                        value = default_value
                    else:
                        print "     - use-default: False"
            else:
                print "     - required: False"
                value_defined_by_user = lookup(component, meta_info['primary_config_key'], config_param)
                if value_defined_by_user != None:
                    print "     - specified: True"
                    value = value_defined_by_user
                    print "     - user-defined-value: " + str(value)
                else:
                    print "     - specified: False"
                    if expected_params[config_param]['use_default']:
                        print "     - use-default: True"
                        default_value = lookup_defaults(defaults_for_expected_params, meta_info, config_param)
                        print "     - default-value: " + str(default_value)
                        value = default_value
                    else:
                        print "     - use-default: False"
                        value = "Ignore"
            print "     - Final Value: " + str(value)
            if value is None:
                message = "A value needs to be specified for " + str(config_param) + " in your site level config file for correctly configuring component "
                raise Exception(message)
                sys.exit(message)
            final_component_data[str(config_param)] = value
        return final_component_data


def process_config_schema(component, config_schema_file, default_data_runtime_file, meta_info_file ):

    config_schema_file = open(config_schema_file.name, 'r')
    config_schema = yaml.load(config_schema_file)
    default_data_file = open(default_data_runtime_file.name, 'r')
    default_data = yaml.load(default_data_file)
    meta_info_file = open(meta_info_file.name, 'r')
    meta_info = yaml.load(meta_info_file)
    expected_params = config_schema['expected-from-site-level-config']
    defaults_for_expected_params = default_data['expected-from-site-level-config']
    final_config_for_component = get_final_config_values_for_component(component, expected_params, defaults_for_expected_params, meta_info)
    print final_config_for_component
    return final_config_for_component


