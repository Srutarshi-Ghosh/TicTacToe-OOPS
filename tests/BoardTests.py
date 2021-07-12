import unittest
from models.Board import Board
from models.GameState import GameState


class MyTestCase(unittest.TestCase):

    def test_set_game_board(self):
        custom_board = [['X', 'X', 'X'], ['O', 'O', 'X'], ['O', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        self.assertEqual(board.game_board, custom_board)

    def test_gamestate(self):
        custom_board = [['X', 'X', 'X'], ['O', 'O', 'X'], ['O', 'O', 'X']]
        board = Board()
        board.set_game_board(custom_board=custom_board)
        game_state = board.get_game_state()
        self.assertEqual(game_state, GameState.WINNER)



if __name__ == '__main__':
    unittest.main()
