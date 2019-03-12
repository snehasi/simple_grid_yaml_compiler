# simple_grid_yaml_compiler
Generates the extended YAML output for an input site_level_configuration_file

# Setup development Environment
You'll need Python 2.7 or higher.
- Fork this repository and clone your fork in your development machine.
- Create a virtualenv with Python >= 2.7 and install all the required packages listed in the requirements.txt file.
- At the root of the directory, create a .temp folder. ```mkdir .temp```
- Create a site_level_configuration_file.yaml in the root directory. You can use the one available in the [puppet module](https://github.com/WLCG-Lightweight-Sites/simple_grid_puppet_module/tree/master/templates).
- Execute the compiler using the following command template from the root directory
```
python simple_grid_yaml_compiler.py {PATH_TO_SITE_LEVEL_CONFIG_FILE} -o {PATH_TO_AUGMENTED_SITE_LEVEL_CONFIG_FILE}
```
For instance, 
```
python simple_grid_yaml_compiler.py ./tests/resources/complete_config.yaml -o ./tests/output.yaml
```
- After running the compiler, the output would be generated at {PATH_TO_AUGMENTED_SITE_LEVEL_CONFIG_FILE}

