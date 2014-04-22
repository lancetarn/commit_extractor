
import os
import ConfigParser
import unittest
import mock
import commitextractor

class CommitExtractorTests(unittest.TestCase):

    def setUp(self):
        config = """[svn]
repo = svn+ssh://fake.svn.repo
start_date = 2013-12-31
end_date = 2014-02-01
[db]
host=localhost
user=fakeuser
pass=fakepass
        """
        bad_config = """[bogus]
stuff = bad
"""
        empty_config = ''

        self.good_cnf_file = os.getcwd() + 'test_cnf.cnf'
        cnf_handle = open(self.good_cnf_file, 'w');
        cnf_handle.write(config)
        cnf_handle.close()

        self.bad_cnf_file = os.getcwd() + 'bad_cnf.cnf'
        cnf_handle = open(self.bad_cnf_file, 'w');
        cnf_handle.write(bad_config)
        cnf_handle.close()

        self.empty_cnf_file = os.getcwd() + 'bad_cnf.cnf'
        cnf_handle = open(self.empty_cnf_file, 'w');
        cnf_handle.write(empty_config)
        cnf_handle.close()

        self.commit_extractor  =  commitextractor.CommitExtractor()


    def test_cnf_set(self):
         self.commit_extractor._parse_config(self.good_cnf_file)
         svn_cnf = {
             "repo": "svn+ssh://fake.svn.repo",
             "start_date": "2013-12-31",
             "end_date": "2014-02-01"
         }
         self.assertEqual(svn_cnf, self.commit_extractor.svn_cnf)

    def test_missing_config(self):
        fake_path = '/path/is/fake'

        self.assertRaises( commitextractor.NoConfigError, self.commit_extractor._parse_config, fake_path )

    def test_empty_config(self):
        self.assertRaises(ConfigParser.NoSectionError, self.commit_extractor._parse_config, self.empty_cnf_file)

    def test_config_missing_section(self):
        self.assertRaises(ConfigParser.NoSectionError, self.commit_extractor._parse_config, self.bad_cnf_file)



    def test_init_svn_broker(self):
        pass




if __name__ == "__main__":
    unittest.main()
