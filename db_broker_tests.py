import unittest
import mock
import db_broker
import os
from svn_file import SvnFile


class DbBrokerTests(unittest.TestCase):

    def setUp(self):
        self.broker = db_broker.DbBroker(':memory:')
        self.broker.connect()
        script_file = open(os.getcwd() + '/initial_create.sql', 'r')
        script = script_file.read()
        self.broker.cursor.executescript(script)
        self.broker.conn.commit()

        test_file_a = SvnFile()
        test_file_a.set_filename('/some/test/file/path.py')
        test_file_a.set_product('test_product')

        test_file_b = SvnFile()
        test_file_b.set_filename('/some/other/test/file/path.py')
        test_file_b.set_product('second_test_product')

        self.test_files = [test_file_a, test_file_b]

    def test_error_connecting(self):
        self.broker.conn.close()
        self.broker.db_name = '/rootdir.db'
        self.assertRaises(db_broker.sqlite3.OperationalError, self.broker.connect)

    def test_connect_success(self):
        pass

    def test_get_last_rev(self):
        # test None
        # test not None
        # test garbage
        pass

    def test_insert_empty(self):
        pass

    def test_insert_svnfiles(self):
        self.broker.insert_svnfiles(self.test_files)

    def test_insert_duplicate_files(self):
        pass

    def test_insert_duplicate_rev(self):
        pass

if __name__ == "__main__":
    unittest.main()
