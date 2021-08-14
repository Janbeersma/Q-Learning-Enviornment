import gym
import numpy as np

#Maakt een specifieke omgeving aan
env = gym.make("MountainCar-v0")

#reset de omgeving (standaard voor het aanmaken van een omgeving)
env.reset()

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 25000

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE
print(discrete_os_win_size)

q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))
print(q_table.shape)

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))

'''
#goalstate status
done = False

#zolang goalstate niet bereikt is 
while not done:
    #voer actie 2 uit in dit geval ga naar rechts
    action = 2

    new_state, reward, done, _ = env.step(action)
    print(reward, new_state)
    env.render()

env.close()
'''