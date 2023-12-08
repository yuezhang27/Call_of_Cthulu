"""
Add a docstring
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from Main.CallOfCthulu import is_alive_and_sane


class TestIsAliveAndSane(TestCase):
    def test_character_alive_and_sane(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        expected = True
        actual = is_alive_and_sane(character)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_character_dead(self, mock_output):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 0, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        expected = False
        actual = is_alive_and_sane(character)
        expected_output = "You are dead of low HP"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertIn(expected_output, actual_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_character_insane(self, mock_output):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5, "Sanity": 0, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        expected = False
        actual = is_alive_and_sane(character)
        expected_output_one = "You are mad"
        expected_output_two = "All hail Cthulhu"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertIn(expected_output_one, actual_output)
        self.assertIn(expected_output_two, actual_output)
