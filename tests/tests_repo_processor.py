from compiler.repo_processor import analyse_repo_url, generate_default_file_name, generate_config_schema_file_name, generate_meta_info_file_name
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
