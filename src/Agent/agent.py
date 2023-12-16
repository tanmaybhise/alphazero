import sys
sys.path.append(".")

import random

from src.Environment.tic_tac_toe import TicTacToe
from src.Agent.memory import Memory

class Agent():
    def __init__(self, game, whoami, memory) -> None:
        self.game = game
        self.whoami = whoami
        self.memory = memory

    def naive_step(self):
        possible_moves = self.game.get_legal_moves()
        if possible_moves==[]:
            return None
        move = random.choice(possible_moves)
        while ((self.game.player == self.whoami) and\
               (self.game.metadata["terminated"]==False)):
            self.game.make_move(move[0], move[1])
            self.memory.update_agenty_memory(game_state=self.game, agent=self.whoami, move=[move[0], move[1]])


if __name__=="__main__":
    game = TicTacToe(player=1)
    agent1 = Agent(game, whoami=1)
    agent2 = Agent(game, whoami=2)
    while game.metadata["terminated"] == False:
        agent1.naive_step()
        agent2.naive_step()
    print(f"Winner: {game.winner}")
    print(game)