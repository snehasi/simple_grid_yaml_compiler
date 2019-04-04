from compiler.repo_processor import analyse_repo_url, generate_default_file_name, generate_config_schema_file_name, generate_meta_info_file_name, get_default_values, get_config_schema

from os import mkdir
from shutil import rmtree
from urllib2 import urlopen

import unittest

class RepoProcessorTest(unittest.TestCase):
	def test_analyse_repo_url(self):
		repo_url = "https://github.com/WLCG-Lightweight-Sites/simple_grid_yaml_compiler"
		
		expected_output = {
			"org_name": "WLCG-Lightweight-Sites",
			"repo_name": "simple_grid_yaml_compiler",
			"branch_name": "master"
		}

		self.assertDictEqual(analyse_repo_url(repo_url), expected_output)

	def test_generate_default_file_name(self):
		repo_info = {
			"org_name": "WLCG-Lightweight-Sites",
			"repo_name": "simple_grid_yaml_compiler",
			"branch_name": "master"
		}

		expected_output = "./.temp/simple_grid_yaml_compiler_defaults.yaml"

		self.assertEqual(generate_default_file_name(repo_info), expected_output)

	def test_generate_config_schema_file_name(self):
		repo_info = {
			"org_name": "WLCG-Lightweight-Sites",
			"repo_name": "simple_grid_yaml_compiler",
			"branch_name": "master"
		}

		expected_output = "./.temp/simple_grid_yaml_compiler_schema.yaml"

		self.assertEqual(generate_config_schema_file_name(repo_info), expected_output)

	def test_generate_meta_info_file_name(self):
		repo_info = {
			"org_name": "WLCG-Lightweight-Sites",
			"repo_name": "simple_grid_yaml_compiler",
			"branch_name": "master"
		}

		expected_output = "./.temp/simple_grid_yaml_compiler_info.yaml"

		self.assertEqual(generate_meta_info_file_name(repo_info), expected_output)

	def test_get_default_values(self):
		repo_url      = "https://github.com/WLCG-Lightweight-Sites/simple_grid_site_defaults"
		defaults_file = "site_level_configuration_defaults.yaml"

		fname  = get_default_values(repo_url, defaults_file)

		with open(fname, "r") as file:
			output = file.read()

		file_url        = "https://raw.githubusercontent.com/WLCG-Lightweight-Sites/simple_grid_site_defaults/master/site_level_configuration_defaults.yaml"
		expected_output = urlopen(file_url).read()

		self.assertEqual(output, expected_output)

	def test_get_config_schema(self):
		repo_url = "https://github.com/WLCG-Lightweight-Sites/wlcg_lightweight_site_ce_cream"

		repo_info = analyse_repo_url(repo_url)
		fname     = generate_config_schema_file_name(repo_info)

		with open(fname, "r") as file:
			output = file.read()

		file_url = "https://raw.githubusercontent.com/WLCG-Lightweight-Sites/wlcg_lightweight_site_ce_cream/master/config-schema.yaml"
		expected_output = urlopen(file_url).read()

		self.assertEqual(output, expected_output)
