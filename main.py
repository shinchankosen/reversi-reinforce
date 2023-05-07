import gym
import gym_reversi
import random
import numpy as np
env = gym.make('Reversi8x8-v0')
env.reset()
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        enables = env.possible_actions
        # if nothing to do ,select pass
        if len(enables)==0:
            action = env.board_size**2 + 1
        # random select (update learning method here)
        else:
            action = random.choice(enables)
        observation, reward, done, info = env.step(action)
        env.render()
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            black_score = len(np.where(env.state[0,:,:]==1)[0])
            white_score = len(np.where(env.state[0,:,:]==0)[0])
            print(f'black score = {black_score}')
            print(f'white score = {white_score}')
            break
        