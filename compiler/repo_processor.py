import re
import urllib2
from urlparse import urlparse, urljoin


def generate_default_file_name(repo_info):
    return './.temp/' + repo_info['repo_name'] + '_defaults.yaml'


def analyse_repo_url(repo_url):
    print(repo_url)
    repo_analysis = re.search('//.*/(.*)/(.*)', repo_url)
    print(repo_analysis)
    org_name = repo_analysis.group(1)
    repo_name = repo_analysis.group(2)
    ##TODO fetch branch info
    branch = 'master'
    return {
        'org_name':org_name,
        'repo_name': repo_name,
        'branch_name': branch
    }


def get_default_values(repo_url):
    default_data_base_url = urlparse("https://raw.githubusercontent.com/")
    repo_info = analyse_repo_url(repo_url)
    repo_info_list = [repo_info['org_name'], repo_info['repo_name'], repo_info['branch_name'], 'default-data.yaml']
    default_data_relative_url = urlparse("/".join(x.strip() for x in repo_info_list))
    default_data_url = urljoin(default_data_base_url.geturl(), default_data_relative_url.geturl())
    response = urllib2.urlopen(default_data_url)
    default_data = response.read()
    with open(generate_default_file_name(repo_info), 'w') as f:
        f.write(default_data)
        f.close()
