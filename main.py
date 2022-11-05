import os.path

from melee_env.pettingzoo_env import MeleeEnv
from melee_env.agents.basic import *
from melee_env.agents.gymnasium_basic import CPUFox, RandomFox
import argparse

players = [RandomFox(), CPUFox()]
#players = [Random(enums.Character.FOX, press_start=False), Random(enums.Character.FOX, press_start=False)]


env = MeleeEnv(players, os.path.expanduser('~/.melee/SSBM.ciso'), fast_forward=True)

episodes = 10; reward = 0
env.start_emulator()

for episode in range(episodes):
    gamestate, done = env.reset(enums.Stage.FOUNTAIN_OF_DREAMS)
    while not done:
        actions = []
        for player in players:
            if player.agent_type == "CPU":  # CPU actions are handled internally
                action = None
            else:
                action = player.act(gamestate)
            actions.append(action)
        gamestate, done = env.step(actions=actions)
