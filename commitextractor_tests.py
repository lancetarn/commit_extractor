
import os
import unittest
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

        self.cnf_file = os.getcwd() + 'test_cnf.cnf'
        cnf_handle = open(self.cnf_file, 'w');
        cnf_handle.write(config)
        cnf_handle.close()


    def test_cnf_set(self):
         extractor = commitextractor.CommitExtractor()
         extractor.parse_config(self.cnf_file)
         svn_cnf = {
             "repo": "svn+ssh://fake.svn.repo",
             "start_date": "2013-12-31",
             "end_date": "2014-02-01"
         }
         self.assertEqual(svn_cnf, extractor.svn_cnf)



if __name__ == "__main__":
    unittest.main()
