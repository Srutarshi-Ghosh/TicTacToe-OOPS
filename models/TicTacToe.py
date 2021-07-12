from models.Player import Player
from models.Board import Board
from models.GameState import GameState


class TicTacToe:

    def __init__(self):
        self.board = Board()
        self.player1 = Player('Player 1', 'X')
        self.player2 = Player('Player 2', 'O')
        self.current_player = self.player1
        self.game_state = GameState.ONGOING

    def update_board(self, selected_position):
        player_piece = self.current_player.get_game_piece()
        self.board.update_game_board(selected_position, player_piece)

    def get_game_state(self):
        return self.board.get_game_state()

    def switch_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    # def show_board(self):
    #     return self.board.display()

    # @staticmethod
    # def show_game_instructions():
    #     print("\nEnter a value between 1-9: ")
    #     print("Positions of each number are as follows")
    #     print(" 1 | 2 | 3")
    #     print("-----------")
    #     print(" 4 | 5 | 6")
    #     print("-----------")
    #     print(" 7 | 8 | 9\n")

    # def play_game(self):
    #     self.new_game()
    #     game_over = False
    #     game_result = None
    #
    #     while not game_over:
    #         self.show_game_instructions()
    #         self.make_move()
    #         self.show_board()
    #         game_over, game_state = self.check_game_over()
    #         self.switch_player()
    #
    #     print(game_result)

