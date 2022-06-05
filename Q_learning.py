
import gym
import numpy as np
def Qtable(state_space,action_space,bin_size = 30):
    
    bins = [np.linspace(-4.8,4.8,1),
            np.linspace(-4,4,1),
            np.linspace(-0.418,0.418,bin_size),
            np.linspace(-4,4,bin_size)]
    
    q_table = np.random.uniform(low=-1,high=1,size=([bin_size] * state_space + [action_space]))
    return q_table, bins

def Discrete(state, bins):
    index = []
    for i in range(len(state)): index.append(np.digitize(state[i],bins[i]) - 1)
    return tuple(index)
def Q_learning(q_table, bins, episodes = 5000, gamma = 0.95, lr = 0.1, timestep = 10, epsilon = 0.2):
    
    rewards = 0
    steps = 0
    for episode in range(1,episodes+1):
        steps += 1 
        current_state = Discrete(env.reset(),bins)
      
        score = 0
        done = False
        while not done: 
            if episode%timestep==0: env.render()
            if np.random.uniform(0,1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q_table[current_state])
            observation, reward, done, info = env.step(action)
            next_state = Discrete(observation,bins)
            score+=reward
            reward=reward*4-abs(next_state[0])
            if not done:
                max_future_q = np.max(q_table[next_state])
                current_q = q_table[current_state+(action,)]
                new_q = (1-lr)*current_q + lr*(reward + gamma*max_future_q)
                q_table[current_state+(action,)] = new_q
            current_state = next_state
            
        # End of the loop update
        else:
            rewards += score
            if score > 250 and steps >= 100: print('Solved')
        if episode % timestep == 0: print(reward / timestep)
num_steps = 1500
env=gym.make("CartPole-v1")


q_table,bins=Qtable(4,2)
Q_learning(q_table,bins)

env.close()