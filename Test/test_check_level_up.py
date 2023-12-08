"""
Unit Test
check_level_up
"""
from unittest import TestCase

from Main.draft import check_level_up


class TestCheckLevelUp(TestCase):
    def test_leveled_up(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Sanity': 10, 'Experience': 10,
                     'Darkness': 4, 'Level': 2}
        expected = True
        actual = check_level_up(character)
        self.assertEqual(expected, actual)

    def test_not_level_up_low_experience(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Sanity': 10, 'Experience': 9,
                     'Darkness': 4, 'Level': 1}
        expected = False
        actual = check_level_up(character)
        self.assertEqual(expected, actual)

    def test_not_level_up_highest_level(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Sanity': 10, 'Experience': 10,
                     'Darkness': 4, 'Level': 3}
        expected = False
        actual = check_level_up(character)
        self.assertEqual(expected, actual)

    def test_not_level_up_both(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 10, 'Sanity': 10, 'Experience': 9,
                     'Darkness': 4, 'Level': 3}
        expected = False
        actual = check_level_up(character)
        self.assertEqual(expected, actual)
