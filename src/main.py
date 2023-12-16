import os
import sys
sys.path.append(".")

import random
import pandas as pd

from tqdm import tqdm

from src.Environment.tic_tac_toe import TicTacToe
from src.Agent.agent import Agent
from src.Agent.memory import Memory

def main():
    game = TicTacToe(player=1)
    memory = Memory('./src/data')
    agent1 = Agent(game, whoami=1, memory=memory)
    agent2 = Agent(game, whoami=2, memory=memory)
    while game.metadata["terminated"] == False:
        agent1.naive_step()
        agent2.naive_step()
    memory.write_agent_memory(winner=game.winner)

if __name__=="__main__":
    for _ in tqdm(range(10)):
        main()