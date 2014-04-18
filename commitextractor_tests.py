
import os
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

        self.cnf_file = os.getcwd() + 'test_cnf.cnf'
        cnf_handle = open(self.cnf_file, 'w');
        cnf_handle.write(config)
        cnf_handle.close()

        self.ce  =  commitextractor.CommitExtractor()


    def test_cnf_set(self):
         self.ce.parse_config(self.cnf_file)
         svn_cnf = {
             "repo": "svn+ssh://fake.svn.repo",
             "start_date": "2013-12-31",
             "end_date": "2014-02-01"
         }
         self.assertEqual(svn_cnf, extractor.svn_cnf)

    def test_init_svn_broker(self, svn_broker):
        pass




if __name__ == "__main__":
    unittest.main()
