import unittest
from pyutils import get_rel_dir

class TestStringMethods(unittest.TestCase):

    def test_rel_path(self):
        self.assertEqual(get_rel_dir("/somewhere/scripts/live/", "../../results/live/"),
                         "/somewhere/results/live/")

        with self.assertRaises(TypeError):
            get_rel_dir("../../results/live/")

if __name__ == '__main__':
    unittest.main()
