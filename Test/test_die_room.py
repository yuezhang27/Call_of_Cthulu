"""
Unit Test
die_of_rooms
"""

from unittest import TestCase
from unittest.mock import patch

from Main.draft import die_of_rooms


class TestDieOfRooms(TestCase):
    @patch('random.randint', return_value=1)
    def test_totem(self, _):
        expected = "Totem"
        actual = die_of_rooms(3)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=6)
    def test_empty_room(self, _):
        expected = "empty room"
        actual = die_of_rooms(2)
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=8)
    def test_runes(self, _):
        expected = "runes"
        actual = die_of_rooms(1)
        self.assertEqual(actual, expected)
