from compiler import lexemes, semantics, yaml_augmentation, repo_processor, runtime_variables
import argparse
import yaml


## fetch repos, add include statement for the downloaded default_values.yaml
def phase_1(site_level_configuration_file, main_default_values_file):
    ## fetch repo and get default_values.yaml
    repo_urls = lexemes.get_repo_list(site_level_configuration_file)
    print(repo_urls)
    file_names_repository_default = [main_default_values_file]
    for url in repo_urls:
        file_names_repository_default.append(repo_processor.get_default_values(url))

    default_includes_yaml_file = yaml_augmentation.add_include_statements_for_default_files(file_names_repository_default, site_level_configuration_file)
    return default_includes_yaml_file

def phase_two_and_a_half(include_made):
    return runtime_variables.add_runtime_variables(include_made)

## add data from all includes
def phase_2(default_includes_yaml_file):
    return yaml_augmentation.add_included_files(default_includes_yaml_file)



## syntax_checking
def phase_3(final_yaml_file):
    return semantics.check_yaml_syntax(final_yaml_file)

def phase_4(phase_3_output):
    pass

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    return {
        'site_level_configuration_file': args.filename,
        'output': args.output
    }

if __name__ == "__main__":

    args = parse_args()
    site_level_configuration_file = open(args['site_level_configuration_file'], 'r')
    main_default_values_file = "./tests/resources/default_values.yaml"
    output = open(args['output'], 'w')
    default_includes_yaml_file = phase_1(site_level_configuration_file, main_default_values_file)
    include_made = phase_2(default_includes_yaml_file)
    print("Phase 2 output")
    print(include_made.name)
    runtime = phase_two_and_a_half(include_made)
    augmented_yaml_file = phase_3(runtime, output)
    # augmented_yaml_file = phase_3(open('./.temp/runtime.yaml', 'r'), output)
    augmented_yaml_file = open(augmented_yaml_file.name, 'r')
    data =yaml.load(augmented_yaml_file)
    print data['lightweight_components'][0]['config']['cream-info']['ce_cpu_model']
    print data['supported_virtual_organizations']
    print data['site']['latitude']
    phase_4(augmented_yaml_file)
