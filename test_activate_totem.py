"""
Add a docstring
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from draft import activate_totem


class TestActivateTotem(TestCase):
    @patch('builtins.input', side_effect=["at"])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_activate_totem_success(self, mock_stdout, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Sanity': 10, 'Experience': 0,
                     'Darkness': 3, 'Level': 1}
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4, 'Sanity': 10, 'Experience': 1,
                              'Darkness': 3, 'Level': 1}
        expected_output = "Totem activated\n"
        actual_character = activate_totem(character)
        actual_output = mock_stdout.getvalue()
        self.assertEqual(expected_character, actual_character)
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=["at"])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_activate_totem_failure(self, mock_stdout, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Sanity': 10, 'Experience': 0,
                     'Darkness': 3, 'Level': 1}
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4, 'Sanity': 10, 'Experience': 0,
                              'Darkness': 3, 'Level': 1}
        expected_output = "Totem not activated. Try harder or try another direction\n"
        actual_character = activate_totem(character)
        actual_output = mock_stdout.getvalue()
        self.assertEqual(expected_character, actual_character)
        self.assertEqual(expected_output, actual_output)
