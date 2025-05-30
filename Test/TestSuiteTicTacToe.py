import unittest

from src.TicTacToe import TicTacToe

class TestSuiteTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe()
        return

    def tearDown(self):
        return

    def test_end2end_player1_wins(self):
        #TEST 1
        # Arrange
        tic_tac_toe = TicTacToe()
        player_one_move = (1,1)
        expected_next_player = 'Player2'
        current_player = 'Player1'
        player_character = tic_tac_toe.return_player_symbol(current_player)

        #Act
        tic_tac_toe.play_move(*player_one_move)

        #Assert
        self.assertEqual(player_character, tic_tac_toe.determine_cell_occupant((1, 1)))
        self.assertIsNone(tic_tac_toe.check_end_of_game())
        self.assertEqual(expected_next_player, tic_tac_toe.get_active_player())

        #TEST 2
        #Arrange
        player_two_move = (1,0)
        expected_next_player = 'Player1'
        current_player = 'Player2'
        player_character = tic_tac_toe.return_player_symbol(current_player)

        #Act
        tic_tac_toe.play_move(*player_two_move)

        #Assert
        self.assertEqual(player_character, tic_tac_toe.determine_cell_occupant((1, 0)))
        self.assertIsNone(tic_tac_toe.check_end_of_game())
        self.assertEqual(expected_next_player, tic_tac_toe.get_active_player())

        #TEST 3
        #Arrange
        player_one_move = (0,0)
        player_two_move = (0,1)
        expected_next_player = 'Player1'

        #Act
        tic_tac_toe.play_move(*player_one_move)
        tic_tac_toe.play_move(*player_two_move)

        #Assert
        self.assertIsNone(tic_tac_toe.check_end_of_game())
        self.assertEqual(expected_next_player, tic_tac_toe.get_active_player())

        #TEST 3
        #Arrange
        player_one_move = (2,2)
        expected_winner = 'Player1'

        #Act
        tic_tac_toe.play_move(*player_one_move)

        #Assert
        self.assertIsNotNone(tic_tac_toe.check_end_of_game())
        self.assertEqual(f"{expected_winner} wins", tic_tac_toe.check_end_of_game())

        return

    def test_end2end_game_drawn(self):
        #TEST 1
        #Arrange
        tic_tac_toe = TicTacToe()
        player_one_move = (0,0)
        player_two_move = (0,1)

        #Act
        tic_tac_toe.play_move(*player_one_move)
        tic_tac_toe.play_move(*player_two_move)

        #Assert
        self.assertIsNone(tic_tac_toe.check_end_of_game())

        # TEST 2
        # Arrange
        player_one_move = (0, 2)
        player_two_move = (1, 0)

        # Act
        tic_tac_toe.play_move(*player_one_move)
        tic_tac_toe.play_move(*player_two_move)

        # Assert
        self.assertIsNone(tic_tac_toe.check_end_of_game())

        # TEST 3
        # Arrange
        player_one_move = (1, 2)
        player_two_move = (1, 1)

        # Act
        tic_tac_toe.play_move(*player_one_move)
        tic_tac_toe.play_move(*player_two_move)

        # Assert
        self.assertIsNone(tic_tac_toe.check_end_of_game())

        # TEST 4
        # Arrange
        player_one_move = (2, 1)
        player_two_move = (2, 2)

        # Act
        tic_tac_toe.play_move(*player_one_move)
        tic_tac_toe.play_move(*player_two_move)

        # Assert
        self.assertIsNone(tic_tac_toe.check_end_of_game())

        # TEST 5
        # Arrange
        player_one_move = (2, 0)

        # Act
        tic_tac_toe.play_move(*player_one_move)

        # Assert
        self.assertIsNotNone(tic_tac_toe.check_end_of_game())
        self.assertEqual("Draw", tic_tac_toe.check_end_of_game())

        return