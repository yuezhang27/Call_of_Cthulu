"""
Unit Test
move_character
"""
from unittest import TestCase

from Main.CallOfCthulu import move_character


class TestMoveCharacter(TestCase):
    def test_move_north(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 1
        move_character(character, direction)
        expected = {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                    "Darkness": 4, "Level": 1}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_south(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 2
        move_character(character, direction)
        expected = {"X-coordinate": 3, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                    "Darkness": 4, "Level": 1}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_west(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 3
        move_character(character, direction)
        expected = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 10, "Sanity": 10, "Experience": 0,
                    "Darkness": 4, "Level": 1}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_east(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 4
        move_character(character, direction)
        expected = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 10, "Sanity": 10, "Experience": 0,
                    "Darkness": 4, "Level": 1}
        actual = character
        self.assertEqual(expected, actual)
