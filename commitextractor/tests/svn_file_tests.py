import unittest
import svn_file

class SvnFileTests(unittest.TestCase):

    def setUp(self):
        self.filename = 'test/file/name.txt'
        self.product = 'test'
        self.id = 1
        self.svn_file = svn_file.SvnFile()

    def test_set_filename(self):
        self.svn_file.set_filename(self.filename)
        self.assertEquals(self.filename, self.svn_file.filename)

    def test_empty_filename(self):
        # Empty filename
        name = ''
        self.assertRaises(svn_file.BadFilenameError, self.svn_file.set_filename, name)

    def test_bad_filename(self):
        # Bad filename
        name = ['weird']
        self.assertRaises(svn_file.BadFilenameError, self.svn_file.set_filename, name)


    def test_set_product(self):
        self.svn_file.set_product(self.product)
        self.assertEquals(self.product, self.svn_file.product)

    def test_empty_product(self):
        # Empty product
        name = ''
        self.assertRaises(svn_file.BadProductError, self.svn_file.set_product, name)

    def test_bad_product(self):
        # Bad product
        name = ['weird']
        self.assertRaises(svn_file.BadProductError, self.svn_file.set_product, name)


    def test_set_id(self):
        self.svn_file.set_id(self.id)
        self.assertEquals(self.id, self.svn_file.id)

    def test_empty_id(self):
        # Empty id
        id = None
        self.assertRaises(TypeError, self.svn_file.set_id, id)

    def test_bad_id(self):
        # Bad id
        id = ['weird']
        self.assertRaises(TypeError, self.svn_file.set_id, id)

    def test_negative_id(self):
        # Negative
        id = -1
        self.assertRaises(ValueError, self.svn_file.set_id, id)


if __name__ == "__main__":
    unittest.main()
