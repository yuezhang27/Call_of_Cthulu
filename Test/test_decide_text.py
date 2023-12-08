"""
Unit Test
decide_text
"""
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from Main.CallOfCthulu import decide_text


class TestDecideText(TestCase):
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=StringIO)
    def test_text_output_1(self, mock_output, _):
        decide_text()
        expected_text = "I hear the whispers of the stars"
        actual_text = mock_output.getvalue()
        self.assertIn(expected_text, actual_text)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=StringIO)
    def test_text_output_2(self, mock_output, _):
        decide_text()
        expected_text = "Time is melting before my eyes"
        actual_text = mock_output.getvalue()
        self.assertIn(expected_text, actual_text)

    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=StringIO)
    def test_text_output_3(self, mock_output, _):
        decide_text()
        expected_text = "Akhamna, Igwatius"
        actual_text = mock_output.getvalue()
        self.assertIn(expected_text, actual_text)

    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=StringIO)
    def test_text_output_4(self, mock_output, _):
        decide_text()
        expected_text = "All is in vain"
        actual_text = mock_output.getvalue()
        self.assertIn(expected_text, actual_text)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=StringIO)
    def test_text_output_5(self, mock_output, _):
        decide_text()
        expected_text = "I am unsure what is real anymore"
        actual_text = mock_output.getvalue()
        self.assertIn(expected_text, actual_text)

    @patch('random.randint', return_value=6)
    @patch('sys.stdout', new_callable=StringIO)
    def test_text_output_6(self, mock_output, _):
        decide_text()
        expected_text = "Other worlds are calling me"
        actual_text = mock_output.getvalue()
        self.assertIn(expected_text, actual_text)
