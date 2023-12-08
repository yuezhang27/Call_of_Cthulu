"""
Add a docstring
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from Main.CallOfCthulu import mad_or_prophet


class TestMadOrProphet(TestCase):
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_meet_madness(self, mock_output, _):
        level = 1
        expected = "Madness"
        actual = mad_or_prophet(level)
        print_message = mock_output.getvalue()
        expected_message = "When you turn the corner"
        self.assertIn(expected_message, print_message)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=7)
    @patch('sys.stdout', new_callable=StringIO)
    def test_meet_prophet(self, mock_output, _):
        level = 2
        expected = "Prophet"
        actual = mad_or_prophet(level)
        print_message = mock_output.getvalue()
        expected_message = "As you navigate the misty streets"
        self.assertIn(expected_message, print_message)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=StringIO)
    def test_meet_nobody(self, mock_output, _):
        level = 3
        expected = "Nobody"
        actual = mad_or_prophet(level)
        print_message = mock_output.getvalue()
        expected_message = "The streets are eerily empty."
        self.assertIn(expected_message, print_message)
        self.assertEqual(expected, actual)
