import unittest
from models.Board import Board
from models.GameState import GameState


class MyTestCase(unittest.TestCase):

    def test_to_check_if_board_is_set_correctly_when_custom_board_parameter_is_passed(self):
        custom_board = [['X', 'X', 'X'], ['O', 'O', 'X'], ['O', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        self.assertEqual(board.game_board, custom_board)

    def test_gamestate_winner(self):
        custom_board = [['X', 'X', 'X'], ['O', 'O', 'X'], ['O', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        game_state = board.get_game_state()
        self.assertEqual(game_state, GameState.WINNER)

    def test_gamestate_draw(self):
        custom_board = [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        game_state = board.get_game_state()
        self.assertEqual(game_state, GameState.DRAW)

    def test_gamestate_ongoing(self):
        custom_board = [['X', 'X', 'O'], ['O', 'O', 'X'], ['7', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        game_state = board.get_game_state()
        self.assertEqual(game_state, GameState.ONGOING)




if __name__ == '__main__':
    unittest.main()
