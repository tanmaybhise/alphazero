import sys
sys.path.append(".")

import random

from src.Environment.tic_tac_toe import TicTacToe
from src.Agent.memory import Memory
from src.Agent.mcts import Node
from src.Agent.mcts import MCTS
from src.Agent.naive_agent import NaiveAgent

class MCTSAgent():
    def __init__(self, game, whoami, memory) -> None:
        self.game = game
        self.whoami = whoami
        self.memory = memory
    
    def mcts_move(self):
        node = Node(self.game)
        mcts = MCTS(node)
        mcts.main()
        best_move, best_child = node.get_best_child()
        return best_move

    def step(self):
        move = self.mcts_move()
        while ((self.game.player == self.whoami) and\
               (self.game.metadata["terminated"]==False) and\
                move is not None):
            self.game.make_move(move[0], move[1])
            self.memory.update_agenty_memory(game_state=self.game, 
                                             agent=self.whoami, 
                                             move=[move[0], move[1]],
                                             agent_kind="mcts")


if __name__=="__main__":
    game = TicTacToe(player=1)
    memory = Memory("./src/data")
    agent1 = MCTSAgent(game, whoami=1, memory=memory)
    agent2 = NaiveAgent(game, whoami=2, memory=memory)
    while game.metadata["terminated"] == False:
        agent1.step()
        agent2.step()
    print(f"Winner: {game.winner}")
    print(game)