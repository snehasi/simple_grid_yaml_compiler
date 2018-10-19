import re
import urllib2
from urlparse import urlparse, urljoin


def generate_default_file_name(repo_info):
    return './.temp/' + repo_info['repo_name'] + '_defaults.yaml'


def generate_config_schema_file_name(repo_info):
    return './.temp/' + repo_info['repo_name'] + '_schema.yaml'


def generate_meta_info_file_name(repo_info):
    return './.temp/' + repo_info['repo_name'] + '_info.yaml'


def analyse_repo_url(repo_url):
    repo_analysis = re.search('//.*/(.*)/(.*)', repo_url)
    org_name = repo_analysis.group(1)
    repo_name = repo_analysis.group(2)
    ##TODO fetch branch info
    branch = 'master'
    return {
        'org_name':org_name,
        'repo_name': repo_name,
        'branch_name': branch
    }


def get_meta_info(repo_url):
    try:
        base_url = urlparse("https://raw.githubusercontent.com/")
        repo_info = analyse_repo_url(repo_url)
        repo_info_list = [repo_info['org_name'], repo_info['repo_name'], repo_info['branch_name'], 'meta-info.yaml']
        relative_url = urlparse("/".join(x.strip() for x in repo_info_list))
        meta_info_url = urljoin(base_url.geturl(), relative_url.geturl())
        response = urllib2.urlopen(meta_info_url)
        meta_info = response.read()
        fname = generate_meta_info_file_name(repo_info)
        with open(fname, 'w') as f:
            f.write(meta_info)
            f.close()
            return f
    except Exception as ex:
        print ex.message


def get_default_values(repo_url, default_file_name):
   try:
        default_data_base_url = urlparse("https://raw.githubusercontent.com/")
        repo_info = analyse_repo_url(repo_url)
        repo_info_list = [repo_info['org_name'], repo_info['repo_name'], repo_info['branch_name'], default_file_name]
        default_data_relative_url = urlparse("/".join(x.strip() for x in repo_info_list))
        default_data_url = urljoin(default_data_base_url.geturl(), default_data_relative_url.geturl())
        response = urllib2.urlopen(default_data_url)
        default_data = response.read()
        fname = generate_default_file_name(repo_info)
        with open(fname, 'w') as f:
            f.write(default_data)
            f.close()
        # process runtime variables
        runtime_variables = get_runtime_variables(fname)
        return fname
   except Exception as ex:
       print(ex.message)


def get_config_schema(repo_url):
    try:
        base_url= urlparse("https://raw.githubusercontent.com/")
        repo_info = analyse_repo_url(repo_url)
        repo_info_list = [repo_info['org_name'], repo_info['repo_name'], repo_info['branch_name'], 'config-schema.yaml']
        relative_url = urlparse("/".join(x.strip() for x in repo_info_list))
        config_schema_url = urljoin(base_url.geturl(), relative_url.geturl())
        response = urllib2.urlopen(config_schema_url)
        config_schema = response.read()
        fname = generate_config_schema_file_name(repo_info)
        with open(fname, 'w') as f:
            f.write(config_schema)
            f.close()
            return f
    except Exception as ex:
        print(ex.message)


def get_runtime_variables(fname):
    f = open(fname, 'r')
    for l in f.readlines():
        re.search("runtime-variable-mapping:", l)
        """
        runtime-variable-mapping:
            - &ce_host lightweight-component[name='cream'][type='compute-element'][]
        """
