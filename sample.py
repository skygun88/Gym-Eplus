import os
import sys
import gym


import eplus_env



if __name__ == "__main__":
    env = gym.make('Eplus-demo-v2')

    curSimTime, ob, isTerminal = env.reset()

    for _ in range(20):
        set_points = [25, 25]
        ts, ob, isTerminal, additional = env.step(set_points)
        print(ob)

    # print(curSimTime, ob, isTerminal)