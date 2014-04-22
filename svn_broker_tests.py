import svn_broker
import pysvn
import unittest
import mock
import pprint
import time


class SvnBrokerTests(unittest.TestCase):
    """
    Using SSH keys; not worrying about user credential tests.
    Future test: Connection timeout
    """

    def setUp(self):

        test_time = float(123456)
        test_files = ['test/file/one.txt', 'test/file/two.txt']
        self.good_log = {
            4: {
                'time': time.localtime(test_time),
                'files': test_files
            }
        }

        self.revision = mock.MagicMock()
        self.revision.number = 4
        log_dict = {
                'author': 'Test Author',
                'date': test_time,
                'message': 'Test Log Message',
                'revision': self.revision,
                'changed_paths': [
                    {'path': test_files[0], 'action': 'A', 'copyfrom_path': None, 'copyfrom_revision': None},
                    {'path': test_files[1], 'action': 'M', 'copyfrom_path': None, 'copyfrom_revision': None}
                ]
            }

        self.raw_log = pysvn.PysvnLog(log_dict)
        mock_client = mock.MagicMock()
        mock_client.log = mock.MagicMock(return_value=[self.raw_log])
        self.mock_client = mock_client
        self.svn_broker = svn_broker.SvnBroker('svn+ssh://fake/repo', self.mock_client)

    def test_repo_not_exists(self):
        pass

    def test_returns_one_log(self):
        self.assertEquals([self.good_log], self.svn_broker.get_logs(None, None))

    def test_returns_two_logs(self):
        pass

    def test_returns_no_logs(self):
        self.mock_client.log = mock.MagicMock(return_value=[])
        self.assertEquals([], self.svn_broker.get_logs(None, None))

    def test_returns_duplicate_logs(self):
        pass

    def test_rev_no_files(self):
        # Raise exception
        pass

# Just to see the real thing...
#    def test_real_connection(self):
#        url = 'svn+ssh://svn.clockwork.net/svnroot/code/products/amm/branches/openid-pre-namespace'
#        self.svn_broker.client = pysvn.Client()
#        self.svn_broker.repo_url = url
#        logs = self.svn_broker.get_logs(None, None)
#
#        pp = pprint.PrettyPrinter(indent=4)
#        pp.pprint(logs)



if __name__ == "__main__":
    unittest.main()
