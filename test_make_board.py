"""
Unit Test:
make_board
"""
from unittest import TestCase
from unittest.mock import patch

from draft import make_board


class TestMakeBoard(TestCase):
    @patch('draft.die_of_rooms', return_value="empty room")
    def test_make_board_level_two(self, _):
        expected = {(0, 0): 'empty room',
                    (0, 2): 'empty room',
                    (0, 1): 'empty room',
                    (0, 3): 'empty room',
                    (0, 4): 'empty room',
                    (1, 0): 'empty room',
                    (1, 1): 'empty room',
                    (1, 2): 'empty room',
                    (1, 3): 'empty room',
                    (1, 4): 'empty room',
                    (2, 0): 'empty room',
                    (2, 1): 'empty room',
                    (2, 2): 'empty room',
                    (2, 3): 'empty room',
                    (2, 4): 'empty room',
                    (3, 0): 'empty room',
                    (3, 1): 'empty room',
                    (3, 2): 'empty room',
                    (3, 3): 'empty room',
                    (3, 4): 'empty room',
                    (4, 0): 'empty room',
                    (4, 1): 'empty room',
                    (4, 2): 'empty room',
                    (4, 3): 'empty room',
                    (4, 4): 'empty room'}
        actual = make_board(2)
        self.assertEqual(expected, actual)

    @patch('draft.die_of_rooms', return_value="runes")
    def test_make_board_level_one(self, _):
        expected = {(0, 0): 'empty room',
                    (0, 1): 'runes',
                    (0, 2): 'runes',
                    (0, 3): 'runes',
                    (0, 4): 'runes',
                    (1, 0): 'runes',
                    (1, 1): 'runes',
                    (1, 2): 'runes',
                    (1, 3): 'runes',
                    (1, 4): 'runes',
                    (2, 0): 'runes',
                    (2, 1): 'runes',
                    (2, 2): 'runes',
                    (2, 3): 'runes',
                    (2, 4): 'runes',
                    (3, 0): 'runes',
                    (3, 1): 'runes',
                    (3, 2): 'runes',
                    (3, 3): 'runes',
                    (3, 4): 'runes',
                    (4, 0): 'runes',
                    (4, 1): 'runes',
                    (4, 2): 'runes',
                    (4, 3): 'runes',
                    (4, 4): 'runes'}
        actual = make_board(1)
        self.assertEqual(expected, actual)

    @patch('draft.die_of_rooms', return_value="Totem")
    def test_make_board_level_three(self, _):
        expected = {(0, 0): 'empty room',
                    (0, 1): 'Totem',
                    (0, 2): 'Totem',
                    (0, 3): 'Totem',
                    (0, 4): 'Totem',
                    (1, 0): 'Totem',
                    (1, 1): 'Totem',
                    (1, 2): 'Totem',
                    (1, 3): 'Totem',
                    (1, 4): 'Totem',
                    (2, 0): 'Totem',
                    (2, 1): 'Totem',
                    (2, 2): 'Totem',
                    (2, 3): 'Totem',
                    (2, 4): 'Totem',
                    (3, 0): 'Totem',
                    (3, 1): 'Totem',
                    (3, 2): 'Totem',
                    (3, 3): 'Totem',
                    (3, 4): 'Totem',
                    (4, 0): 'Totem',
                    (4, 1): 'Totem',
                    (4, 2): 'Totem',
                    (4, 3): 'Totem',
                    (4, 4): 'Totem'}
        actual = make_board(3)
        self.assertEqual(expected, actual)
