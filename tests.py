import unittest
from gaexperiment import GaExperiment, EXPERIMENT_JS


class GaExperimentTests(unittest.TestCase):
    def setUp(self):
        self.sut = GaExperiment('acode', ['v2', 'v3'], {})
    
    def test_is_original_version_in_original_page(self):
        self.assertTrue(self.sut.is_original_version)

    def test_is_original_version_in_variation_page(self):
        self.sut.get_vars = {'gaexp': 'v2'}
        self.assertFalse(self.sut.is_original_version)

    def test_template_to_serve_original_version(self):
        self.assertEqual('abc.pt', self.sut.template_to_serve('abc.pt'))

    def test_template_to_serve_not_in_whitelist(self):
        self.sut.get_vars = {'gaexp': 'v4'}
        self.assertEqual('abc.pt', self.sut.template_to_serve('abc.pt'))

    def test_template_to_serve_in_whitelist(self):
        self.sut.get_vars = {'gaexp': 'v2'}
        self.assertEqual('abc_v2.pt', self.sut.template_to_serve('abc.pt'))

    def test_code_with_variation_page(self):
        self.sut.get_vars = {'gaexp': 'v2'}
        self.assertEqual(
            '<!-- Google Experiments Variation Page -->',
            self.sut.code)

    def test_code_should_be_displayed(self):
        self.assertEqual(
            EXPERIMENT_JS % {'experiment_code': 'acode'},
            self.sut.code)
