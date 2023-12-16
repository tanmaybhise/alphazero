import sys
sys.path.append(".")

import random

from src.Environment.tic_tac_toe import TicTacToe
from src.Agent.memory import Memory
from src.Agent.mcts import Node
from src.Agent.mcts import MCTS

class NaiveAgent():
    def __init__(self, game, whoami, memory) -> None:
        self.game = game
        self.whoami = whoami
        self.memory = memory

    def naive_move(self):
        possible_moves = self.game.get_legal_moves()
        if possible_moves==[]:
            return None
        move = random.choice(possible_moves)
        return move

    def step(self):
        move = self.naive_move()
        while ((self.game.player == self.whoami) and\
               (self.game.metadata["terminated"]==False) and\
                move is not None):
            self.game.make_move(move[0], move[1])
            self.memory.update_agenty_memory(game_state=self.game, 
                                             agent=self.whoami, 
                                             move=[move[0], move[1]],
                                             agent_kind="naive")


if __name__=="__main__":
    game = TicTacToe(player=1)
    memory = Memory("./src/data")
    agent1 = NaiveAgent(game, whoami=1, memory=memory)
    agent2 = NaiveAgent(game, whoami=2, memory=memory)
    while game.metadata["terminated"] == False:
        agent1.step()
        agent2.step()
    print(f"Winner: {game.winner}")
    print(game)