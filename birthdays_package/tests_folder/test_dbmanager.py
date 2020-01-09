import unittest
import dbmanager


class DbmanagerMain(unittest.TestCase):

    def setUp(self):
        self.string_test = 'test'
        self.hash_test = '''7a40954160f1d2a90883c9d6da64aa805085a997fd222e96ee31441d8d35b05b'''

    def test_correct_hash(self):
        computed_hash = dbmanager.compute_n_hashings(self.string_test, 100)
        self.assertEqual(computed_hash, self.hash_test)
