import unittest
import os
from birthdays_package.pyscripts.data_reader import parse_allowed_people


class Test_data_reader(unittest.TestCase):

    def setUp(self):
        self.tmp_file = '/tmp/temporary_file'
        f = open(self.tmp_file, 'w')
        f.close()

    def test_empty_datafile(self):
        df = parse_allowed_people(datafile=self.tmp_file)
        self.assertFalse(df)

    def test_file_is_not_csv(self):
        df = parse_allowed_people(datafile=self.tmp_file)
        self.assertFalse(df)
        
    def test_no_datafile(self):
        df = parse_allowed_people(datafile="/tmp/file_that_does_not_exist")
        self.assertFalse(df)

    def tearDown(self):
        os.remove(self.tmp_file)