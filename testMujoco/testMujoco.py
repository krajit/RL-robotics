# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 07:12:22 2024

@author: sneh.lata
"""

import matplotlib.pyplot as plt
import time
from IPython.display import clear_output
from IPython import display


import gymnasium as gym
#env = gym.make("LunarLander-v2", render_mode="rgb_array")
#env = gym.make("Ant-v4", render_mode = "rgb_array")
#env = gym.make("InvertedPendulum-v4", render_mode = "rgb_array")
#env = gym.make("Pusher-v4", render_mode = "rgb_array")
#env = gym.make("Reacher-v4", render_mode = "rgb_array")
#env = gym.make("Swimmer-v4", render_mode = "rgb_array")  # does not work. Requires some XML file
#env = gym.make("Hopper-v4", render_mode = "rgb_array")
#env = gym.make("Walker2d-v4", render_mode = "rgb_array")
#env = gym.make("Humanoid-v4", render_mode = "rgb_array")
env = gym.make("HalfCheetah-v4", render_mode = "rgb_array")



observation, info = env.reset()

plt.imshow(env.render())
    
#plt.show()

for _ in range(1000):
    plt.cla()

    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    plt.imshow(env.render())
    
    time.sleep(0.01)
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.gcf()
    if terminated or truncated:
        observation, info = env.reset()
        print("terminated. Exiting")
        break
    

env.close()