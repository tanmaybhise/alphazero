import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

class TicTacToe():
    def __init__(self, player=None) -> None:
        self.game_state = np.zeros(9).reshape(3,3)
        self.winner = None
        if player:
            self.player = player
        else:
            self.player = np.random.choice([1,2])

        self.metadata = {"terminated": False}

    def get_legal_moves(self):
        return np.argwhere(self.game_state==0).tolist()
    
    def make_move(self, row, column):
        if [row, column] in self.get_legal_moves():
            self.game_state[row, column] = self.player
            self.winner = self.check_winner()
            self.player = [1 if self.player==2 else 2][0]

    def check_winner(self):
        if (
            ((np.sum(self.game_state == 1, axis=0) == 3).any()) \
            or ((np.sum(self.game_state == 1, axis=1) == 3).any()) \
            or ((self.game_state.diagonal() == 1).all()) \
            or ((np.fliplr(self.game_state).diagonal() == 1).all())
            ):
            self.metadata["terminated"] = True
            return 1

        elif (
            ((np.sum(self.game_state == 2, axis=0) == 3).any()) \
            or ((np.sum(self.game_state == 2, axis=1) == 3).any()) \
            or ((self.game_state.diagonal() == 2).all()) \
            or ((np.fliplr(self.game_state).diagonal() == 2).all())
            ):
            self.metadata["terminated"] = True
            return 2

        elif np.where(self.game_state==0, 1, 0).sum() == 0:
            self.metadata["terminated"] = True
            return 0

        else:
            return None
    
    def __repr__(self) -> str:
        repr = ""
        for i in np.flipud(self.game_state):
            repr+=str(i)+"\n"
        return repr
