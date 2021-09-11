import unittest
from pyutils import get_rel_path
import os

class TestStringMethods(unittest.TestCase):

    def test_rel_path(self):
        self.assertEqual(get_rel_path("/somewhere/scripts/live/", "../../results/live/"),
                         "/somewhere/results/live/")

        with self.assertRaises(TypeError):
            get_rel_path("../../results/live/")

if __name__ == '__main__':
    unittest.main()
