import os.path

from melee_env.env import MeleeEnv
from melee_env.agents.basic import *
import argparse

players = [Rest(), NOOP(enums.Character.FOX)]

env = MeleeEnv(os.path.expanduser('~/.melee/SSBM.ciso'), players, fast_forward=True)

episodes = 10; reward = 0
env.start()

for episode in range(episodes):
    gamestate, done = env.setup(enums.Stage.FINAL_DESTINATION)
    while not done:
        for i in range(len(players)):
            players[i].act(gamestate)
        gamestate, done = env.step()