"""
Unit Test
read_runes
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from Main.CallOfCthulu import read_runes


class TestReadRunes(TestCase):
    @patch('builtins.input', side_effect=["rr"])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_read_runes_success(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10,
                     'Sanity': 10, 'Experience': 0, 'Darkness': 4, 'Level': 1}
        updated_character = read_runes(character)
        output_message = mock_output.getvalue()
        expected_message = ("Runes read. You hear the whispers of the stars, "
                            "speaking of eternal darkness and the endless void.")
        self.assertIn(expected_message, output_message)
        self.assertEqual(updated_character['Sanity'], 9)
        self.assertEqual(updated_character['Experience'], 2)

    @patch('builtins.input', side_effect=["rr"])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_read_runes_failure(self, mock_output, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10,
                     'Sanity': 10, 'Experience': 0, 'Darkness': 4, 'Level': 1}
        updated_character = read_runes(character)
        output_message = mock_output.getvalue()
        expected_message = "You can't read the runes. 'Weird place.' You thought."
        self.assertIn(expected_message, output_message)
        self.assertEqual(updated_character['Sanity'], 10)
        self.assertEqual(updated_character['Experience'], 0)
