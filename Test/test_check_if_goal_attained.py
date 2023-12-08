"""
Add a docstring
"""
from unittest import TestCase

from Main.CallOfCthulu import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_arrived_goal_coordinate(self):
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        expected = True
        actual = check_if_goal_attained(character)
        self.assertEqual(expected, actual)

    def test_not_goal_coordinate_x(self):
        character = {"X-coordinate": 0, "Y-coordinate": 4, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        expected = False
        actual = check_if_goal_attained(character)
        self.assertEqual(expected, actual)

    def test_not_at_goal_coordinate_y(self):
        character = {"X-coordinate": 4, "Y-coordinate": 3, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        expected = False
        actual = check_if_goal_attained(character)
        self.assertEqual(expected, actual)

    def test_not_at_goal_coordinate_both(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 10, "Sanity": 10, "Experience": 0,
                     "Darkness": 4, "Level": 1}
        expected = False
        actual = check_if_goal_attained(character)
        self.assertEqual(expected, actual)
