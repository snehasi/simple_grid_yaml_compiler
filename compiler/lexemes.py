import yaml, re

def get_repo_list(site_level_configuration_file):
    urls = []
    for line in site_level_configuration_file.readlines():
        url_line = re.search('repository_url\w*:\w*(.*)', line)
        if url_line is not None:
            url_line_string = url_line.group()
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url_line_string)
            urls.append(url[0])
    return urls

def include_files(path):
    pass