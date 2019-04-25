from compiler.repo_processor import analyse_repo_url
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
