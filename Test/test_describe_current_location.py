"""
Unit Test:
describe_location_empty
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from Main.CallOfCthulu import describe_current_location


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_describe_location_empty(self, mock_stdout):
        my_board = {
            (0, 0): 'empty room', (0, 1): 'runes', (0, 2): 'Totem', (0, 3): 'empty room', (0, 4): 'runes',
            (1, 0): 'Totem', (1, 1): 'runes', (1, 2): 'runes', (1, 3): 'runes', (1, 4): 'empty room',
            (2, 0): 'runes', (2, 1): 'runes', (2, 2): 'Totem', (2, 3): 'runes', (2, 4): 'runes',
            (3, 0): 'empty room', (3, 1): 'Totem', (3, 2): 'runes', (3, 3): 'runes', (3, 4): 'runes',
            (4, 0): 'runes', (4, 1): 'runes', (4, 2): 'runes', (4, 3): 'Totem', (4, 4): 'empty room'
        }
        my_character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 10, 'Sanity': 10, 'Experience': 0,
                        'Darkness': 4, 'Level': 1}
        expected_output = "Your current location is: \033[91m(0, 1)\033[0m it is: runes\n"
        describe_current_location(my_board, my_character)
        actual_output = mock_stdout.getvalue()
        self.assertEqual(expected_output, actual_output)
