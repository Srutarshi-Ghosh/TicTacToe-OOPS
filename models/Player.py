class Player:

    def __init__(self, name, game_piece):
        self.name = name
        self.game_piece = game_piece

    def get_game_piece(self):
        return self.game_piece

    def get_player_name(self):
        return self.name
