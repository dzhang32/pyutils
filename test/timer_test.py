import unittest
from pyutils import timer

# required to test print()
# https://realpython.com/lessons/mocking-print-unit-tests/
from unittest.mock import patch

@timer(num_times = 5)
def waste_time(n):
    for i in range(n):
        pass

class TestHere(unittest.TestCase):

    def test_timer(self):

        self.assertIsInstance(waste_time(100), float)

    @patch('builtins.print')
    def test_timer_print(self, mock_print):

        waste_time(1)
        mock_print.assert_called_with("Average run time of 'waste_time': 0.0000 s")

if __name__ == '__main__':
    unittest.main()
