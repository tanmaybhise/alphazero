import os
import sys
sys.path.append(".")

import random
import pandas as pd

from tqdm import tqdm

from src.Environment.tic_tac_toe import TicTacToe
from src.Agent.mcts_agent import MCTSAgent
from src.Agent.naive_agent import NaiveAgent
from src.Agent.memory import Memory
from src.Agent.mcts import Node

def main():
    game = TicTacToe(player=1)
    memory = Memory("./src/data")
    agent1 = MCTSAgent(game, whoami=1, memory=memory)
    agent2 = NaiveAgent(game, whoami=2, memory=memory)
    while game.metadata["terminated"] == False:
        agent1.step()
        agent2.step()
    memory.write_agent_memory(winner=game.winner)

if __name__=="__main__":
    for _ in tqdm(range(100)):
        main()