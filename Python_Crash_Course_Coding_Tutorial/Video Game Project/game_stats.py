from score_board import Scoreboard

class GameStats:
    '''Track statistics for Alien invasion'''

    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        #High Score is never to be reset
        self.score_board = Scoreboard
        self.high_score = self.score_board.get_previous_high_score(self)



    def reset_stats(self):
        '''initialize statistics that can change during the game'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

