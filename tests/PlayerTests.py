import unittest
from models.Player import Player

class MyTestCase(unittest.TestCase):

    def test_should_return_player_name(self):
        player_name = 'Player 1'
        player = Player(player_name, 'X')
        self.assertEqual(player_name, player.get_player_name())

    def test_should_return_player_piece(self):
        player_name = 'Player 1'
        player_piece = 'X'
        player = Player(player_name, player_piece)
        self.assertEqual(player_piece, player.get_game_piece())


if __name__ == '__main__':
    unittest.main()
