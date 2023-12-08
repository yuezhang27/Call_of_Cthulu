@patch('builtins.input', side_effect=["1"])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=StringIO)
    def test_guessing_game_wrong(self, mock_output, _, __):
        my_character = {'X-coordinate': 0, 'Y-coordinate': 2, 'Current HP': 5}
        guessing_game(my_character)
        print_message = mock_output.getvalue()
        expected_message = "That is wrong! Pythinx is disappointed\n"
        expected_print_hp = "Your current HP: 4\n"
        self.assertIn(expected_print_hp, print_message)
        self.assertIn(expected_message, print_message)