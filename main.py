import os.path

from melee_env.env import MeleeEnv
from melee_env.agents.basic import *
import argparse

players = [CPU(enums.Character.FOX, 9, press_start=True), CPU(enums.Character.FOX, 9, press_start=False)]

env = MeleeEnv(os.path.expanduser('~/.melee/SSBM.ciso'), players, fast_forward=True)

episodes = 10; reward = 0
env.start_emulator()

for episode in range(episodes):
    gamestate, done = env.reset(enums.Stage.FOUNTAIN_OF_DREAMS)
    while not done:
        for i in range(len(players)):
            players[i].act(gamestate)
        gamestate, done = env.step()