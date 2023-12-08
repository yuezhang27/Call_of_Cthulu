"""
Unit Test
check_learn
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from Main.CallOfCthulu import check_learn


class TestCheckLearn(TestCase):
    @patch('builtins.input', side_effect=["lp"])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_learn_from_prophet(self, mock_output, _, __):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 8, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        level = 2
        check_learn(character, level)
        expected_experience = 2
        expected_sanity = 9
        expected_output = "runes learnt\n"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)
        self.assertEqual(character['Experience'], expected_experience)
        self.assertEqual(character['Sanity'], expected_sanity)

    @patch('builtins.input', side_effect=["lp"])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_not_learn_from_prophet(self, mock_output, _, __):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 8, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        level = 1
        check_learn(character, level)
        expected_experience = 0
        expected_sanity = 8
        expected_output = "runes not learnt\n"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)
        self.assertEqual(character['Experience'], expected_experience)
        self.assertEqual(character['Sanity'], expected_sanity)
