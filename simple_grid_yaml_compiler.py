from compiler import lexemes, semantics, yaml_augmentation, repo_processor

## fetch repos, add include statement for the downloaded default_values.yaml
def phase_1(site_level_configuration_file):
    ## fetch repo and get default_values.yaml
    repo_urls = lexemes.get_repo_list(site_level_configuration_file)
    repo_default_values = {}
    for repo_url in repo_urls:
        default_values = repo_processor.get_default_values()
        repo_default_values += {repo_url: default_values}
    ##
    return yaml_augmentation.add_include_statements_for_default_files()

## add data from all includes
def phase_2(augmented_yaml_file):
    return yaml_augmentation.add_included_files(augmented_yaml_file)

## syntax_checking
def phase_3(final_yaml_file):
    semantics.check_yaml_syntax(final_yaml_file)

if __name__ == "__main__":
    ## process command line arguments
    ## -i site_level_configuration_file
    ## -o optional, save output to specified file
    #phase_3(phase_2(phase_1('input_file')))
    pass