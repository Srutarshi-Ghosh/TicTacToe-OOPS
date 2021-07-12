import unittest
from models.Board import Board
from models.GameState import GameState
from models.Errors import PositionNotValidError


class MyTestCase(unittest.TestCase):

    def test_should_set_game_board_when_custom_board_parameter_is_passed(self):
        custom_board = [['X', 'X', 'X'], ['O', 'O', 'X'], ['O', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        self.assertEqual(board.game_board, custom_board)

    def test_should_return_winner_game_state(self):
        custom_board = [['X', 'X', 'X'], ['O', 'O', 'X'], ['O', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        game_state = board.get_game_state()
        self.assertEqual(game_state, GameState.WINNER)

    def test_should_return_draw_game_state(self):
        custom_board = [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        game_state = board.get_game_state()
        self.assertEqual(game_state, GameState.DRAW)

    def test_should_return_ongoing_game_state(self):
        custom_board = [['X', 'X', 'O'], ['O', 'O', 'X'], ['7', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        game_state = board.get_game_state()
        self.assertEqual(game_state, GameState.ONGOING)

    def test_should_raise_exception_when_invalid_position_is_passed(self):
        position = "10"
        board = Board()
        self.assertRaises(PositionNotValidError, board.update_game_board, position, 'X')

    def test_should_place_piece_when_valid_position_is_passed(self):
        position = "5"
        custom_board = [['X', 'X', 'O'], ['O', '5', 'X'], ['7', 'O', 'X']]
        expected_board = [['X', 'X', 'O'], ['O', 'O', 'X'], ['7', 'O', 'X']]
        piece = 'O'
        board = Board()
        board.set_game_board(custom_board=custom_board)
        board.update_game_board(position, piece)
        self.assertEqual(board.get_game_board(), expected_board)


if __name__ == '__main__':
    unittest.main()
