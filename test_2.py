import gym
import numpy as np

env=gym.make("CartPole-v1")
time_step=200


for i in range(1000):
    current_state=env.reset()

    done= False
    score=0
    while not done:
        if(current_state[0]>0): action =1
        else: action =0
        if i%time_step==0: env.render()
        current_state,reward,done,info=env.step(action)
        score+=reward
        print(score)
    else:
        print("this is changed")
        env.reset()

