## Replace runtime variables with the tag simple-runtime-{varname} and put name in a dict of var,mapped val
## mapped val is determined by yaml search query.
## basically ce_host should be moved to pre-config.py. It can be marked as pre-config.py replacable and therefore it is runtime.
## process the YAML file,
def extract_runtime_variables(includes_made):
    filename = includes_made.name
    site_config_with_includes = open(filename, 'r')
    print("RUNTIME$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    runtime_vars = ""
    config_file = ""
    copy_flag = False
    for line in site_config_with_includes.readlines():

        if copy_flag is True:
            if line.strip().startswith('-'):
                runtime_vars += line
            else:
                copy_flag = False
        else:
            if "runtime_variables" not in line:
                config_file += line
            else:
                runtime_vars += line
                copy_flag = True
    return runtime_vars, config_file


def add_runtime_variables(runtime_vars, config_file):
    output = open('./.temp/runtime.yaml', 'w')
    output.write(runtime_vars + config_file)
    output.close()
    return output

