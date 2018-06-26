def add_include_statements_for_default_files(file_names_repository_default, site_level_configuration_file):
        output = open('./.temp/site_level_configuration_file_unprocessed_includes', 'w')
        for file_name_repository_default in file_names_repository_default:
            try:
                output.write("include: '" + file_name_repository_default + "'\n")
            except Exception as ex:
                print ex.message

        site_level_configuration_file.seek(0)
        output.writelines(l for l in site_level_configuration_file.readlines())
        output.close()
        return output