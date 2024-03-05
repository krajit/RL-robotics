# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 07:12:22 2024

@author: sneh.lata
"""

import matplotlib.pyplot as plt
import time


import gymnasium as gym
#env = gym.make("LunarLander-v2", render_mode="human")
env = gym.make("InvertedPendulum-v4", render_mode = "rgb_array")
observation, info = env.reset()

for _ in range(100):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    plt.imshow(env.render())
    
    plt.show()
    time.sleep(0.01)
    if terminated or truncated:
        observation, info = env.reset()

env.close()