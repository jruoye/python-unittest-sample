from string_formatter import *
import unittest


class TestExecutor(unittest.TestCase):

    def test_upper(self):
        s = 'foo'
        upper_s = upper('foo')
        self.assertEqual(upper_s, 'FOO')


    def test_isupper(self):
        s = 'foo'
        upper_s = upper('foo')
        is_upper_s = isupper(upper_s)
        self.assertTrue(upper_s.isupper())


    def test_isnot_upper(self):
        s = 'foo'
        is_upper_s = isupper(s)
        self.assertFalse(is_upper_s)


    def test_split(self):
        s = 'hello world'
        splitted_s = split(s)
        self.assertEqual(splitted_s, ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(AttributeError):
            split(2)


if __name__ == '__main__':
    unittest.main()
