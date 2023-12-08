"""
Unit Test:
make_character
"""
from unittest import TestCase

from Main.draft import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10,
                    'Sanity': 10, 'Experience': 0, 'Darkness': 4, 'Level': 1}
        actual = make_character()
        self.assertEqual(expected, actual)
