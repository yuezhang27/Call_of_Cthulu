"""
Unit Test
validate_move
"""
from unittest import TestCase

from Main.draft import validate_move


class TestValidateMove(TestCase):
    def test_move_north_valid(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 1
        expected = True
        actual = validate_move(character, direction)
        self.assertEqual(expected, actual)

    def test_move_north_invalid(self):
        character = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 1
        expected = False
        actual = validate_move(character, direction)
        self.assertEqual(expected, actual)

    def test_move_south_valid(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 2
        expected = True
        actual = validate_move(character, direction)
        self.assertEqual(expected, actual)

    def test_move_south_invalid(self):
        character = {"X-coordinate": 4, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 2
        expected = False
        actual = validate_move(character, direction)
        self.assertEqual(expected, actual)

    def test_move_west_valid(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 3
        expected = True
        actual = validate_move(character, direction)
        self.assertEqual(expected, actual)

    def test_move_west_invalid(self):
        character = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 3
        expected = False
        actual = validate_move(character, direction)
        self.assertEqual(expected, actual)

    def test_move_east_valid(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 4
        expected = True
        actual = validate_move(character, direction)
        self.assertEqual(expected, actual)

    def test_move_east_invalid(self):
        character = {"X-coordinate": 2, "Y-coordinate": 4, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        direction = 4
        expected = False
        actual = validate_move(character, direction)
        self.assertEqual(expected, actual)
