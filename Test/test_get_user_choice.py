"""
Unit Test
get_user_choice
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from Main.draft import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["5.5", "0", "hello", "2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_valid(self, mock_output, _):
        expected_choice = 2
        actual_choice = get_user_choice()
        print_message = mock_output.getvalue()
        self.assertEqual(expected_choice, actual_choice)
        self.assertIn("Invalid input. Please enter a number.", print_message)
        self.assertIn("Input must be a number from 1 to 4. Try again.", print_message)
        self.assertIn("You choose to move: South", print_message)
