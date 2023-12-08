"""
Unit Test
check_win
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from Main.CallOfCthulu import check_win


class TestCheckWin(TestCase):
    @patch('builtins.input', side_effect=["fm"])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=StringIO)
    def test_win_fight(self, mock_output, _, __):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 5, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        check_win(character)
        expected_hp = 8
        expected_sanity = 4
        expected_experience = 2
        expected_output = "You won\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(character['Current HP'], expected_hp)
        self.assertEqual(character['Sanity'], expected_sanity)
        self.assertEqual(character['Experience'], expected_experience)

    @patch('builtins.input', side_effect=["fm"])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_lose_fight(self, mock_output, _, __):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 5, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        check_win(character)
        expected_hp = 8
        expected_sanity = 4
        expected_experience = 0
        expected_output = "You lose\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(character['Current HP'], expected_hp)
        self.assertEqual(character['Sanity'], expected_sanity)
        self.assertEqual(character['Experience'], expected_experience)
