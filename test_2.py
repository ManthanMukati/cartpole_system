import re
import gym
import numpy as np
#to generate random qtable and bin to covertion to a fixed values
def QtableandBin():
    bin=(np.linspace(-4.8,4.8,1),np.linspace(-4,4,1),np.linspace(-0.418,0.418,6),np.linspace(-4,4,3))
    qtable=np.random.uniform(-1,1,size=(1,1,6,3,2))
    return qtable,bin

#to convert continues value to discrete    
def Discrete(state, bins):
    index = []
    for i in range(len(state)): index.append(np.digitize(state[i],bins[i])-1)
    return tuple(index)

# setting parameter and envoirment
env=gym.make("CartPole-v1")
c=0
time_step=10
lr=0.1
dis=0.95
exp=0.2
qtable,bin=QtableandBin()
current_state=Discrete(env.reset(),bin)

for i in range(5000):
    
    done= False
    score=0
    while not done:
        
        if i%time_step==0: env.render()
        #choosing to explore or exploit
        print(qtable)
        if np.random.uniform(0,1)<exp:
            action=env.action_space.sample()
        else:
            action=np.argmax(qtable[current_state])
        
        next_state,reward,done,info=env.step(action)
        next_state=Discrete(next_state,bin)
        #upadation eqn
        print(action)
        print(next_state)
        if not done:
            next_max_q=np.max(qtable[next_state])
            current_q=qtable[current_state+(action,)]
            new_q=(1-lr)*current_q+lr*(reward+dis*next_max_q)
            qtable[current_state+(action,)]=new_q
        # else:
        #     qtable[current_state,action]=0
        print("update")
        print(qtable)
        print("Done")
        currunt_state=next_state
        score+=reward
        
    else:
        
         # sucess criteria
        if i%time_step==0:
            print("episode: "+str(i/time_step)+"score: "+str(score))
            if score>=195:
                c+=1
            else:
                c=0
            if c==5:
                print("cong solved ")
            if current_state[2]>0.4:
                print("angle exceeded")
        
        env.reset()
        i=i/time_step

