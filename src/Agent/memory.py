import os
import sys
sys.path.append("..")

import random
import pandas as pd

class Memory():
    def __init__(self, path) -> None:
        self.path = path
        self.initialize_agent_memory()

    def initialize_agent_memory(self):
        if os.path.isfile(f"{self.path}/agent_memory.parquet"):
            self.agent_memory = pd.read_parquet(f"{self.path}/agent_memory.parquet")
        else:
            os.makedirs(self.path, exist_ok=True)
            self.agent_memory = pd.DataFrame()

        if "episode" in self.agent_memory.columns:
            self.episode = self.agent_memory["episode"].max() + 1
        else:
            self.episode=1

    def update_agenty_memory(self, game_state, agent, move, agent_kind):
        inx = self.agent_memory.shape[0]
        self.agent_memory.loc[inx, "game_state"] = str(game_state)
        self.agent_memory.loc[inx, "agent"] = int(agent)
        self.agent_memory.loc[inx, "agent_kind"] = agent_kind
        self.agent_memory.loc[inx, "move"] = str(move)
        self.agent_memory.loc[inx, "episode"] = self.episode
    
    def write_agent_memory(self, winner):
        self.agent_memory.loc[self.agent_memory['episode']==self.episode, 'winner'] = winner
        self.agent_memory.to_parquet(f"{self.path}/agent_memory.parquet")