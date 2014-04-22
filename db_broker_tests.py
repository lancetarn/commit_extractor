import unittest
import mock
import db_broker
from svn_file import SvnFile

class DbBrokerTests(unittest.TestCase):
    def __init__(self):
        pass

    def setUp(self):
        self.broker = db_broker.DbBroker()
        self.broker.cursor = mock.create_autospec(db_broker.sqlite3.Cursor)

        test_file_a = SvnFile()
        test_file_a.set_filename('/some/test/file/path.py')
        test_file_a.set_product('test_product')

        test_file_b = SvnFile()
        test_file_b.set_filename('/some/other/test/file/path.py')
        test_file_b.set_product('second_test_product')

        self.test_files = [test_file_a, test_file_b]

    def test_error_connecting(self):
        #db doesn't exist
        pass

    def test_connect_success(self):
        pass

    def test_get_last_rev(self):
        #test None
        #test not None
        #test garbage
        pass

    def test_insert_empty(self):
        pass

    def test_insert_files(self):
        self.broker


    def test_insert_duplicate_files(self):
        pass

    def test_insert_duplicate_rev(self):
        pass

if __name__ == "__main__":
    unittest.main()
