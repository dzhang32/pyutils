import unittest
import os
from pyutils import here

class TestHere(unittest.TestCase):

    def test_here(self):

        self.assertEqual(here(__file__),
                         os.path.dirname(__file__))

        self.assertEqual(here(__file__, "a", "path"),
                         os.path.join(os.path.dirname(__file__), "a", "path"))

        self.assertEqual(here(__file__, ".."),
                         os.path.abspath(os.path.dirname(__file__) + "/.."))

        self.assertEqual(here(__file__, "..", "file.csv"),
                         os.path.abspath(os.path.dirname(__file__) + "/../file.csv"))

        self.assertEqual(here(__file__, "..", "dir/"),
                         os.path.abspath(os.path.dirname(__file__) + "/../dir") + "/")

    def test_here_errors(self):

        # here() needs input of __file__ manually by
        # the user, if __file__ is default, it will refer to
        # the path to where pyutils.here is defined
        with self.assertRaises(ValueError):
            here()

        with self.assertRaises(TypeError):
            here(1)

        with self.assertRaises(TypeError):
            here(1, 1)

if __name__ == '__main__':
    unittest.main()

