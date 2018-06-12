from compiler import lexemes, semantics, yaml_augmentation, repo_processor
import argparse

## fetch repos, add include statement for the downloaded default_values.yaml
def phase_1(site_level_configuration_file):
    ## fetch repo and get default_values.yaml
    repo_urls = lexemes.get_repo_list(site_level_configuration_file)

    ##
    return yaml_augmentation.add_include_statements_for_default_files(repo_urls, site_level_configuration_file)

## add data from all includes
def phase_2(augmented_yaml_file):
    return yaml_augmentation.add_included_files(augmented_yaml_file)

## syntax_checking
def phase_3(final_yaml_file):
    semantics.check_yaml_syntax(final_yaml_file)

if __name__ == "__main__":
    parser.add_argument('--i')
    args = parser.parse_args()
    phase_3(phase_2(phase_1('input_file')))