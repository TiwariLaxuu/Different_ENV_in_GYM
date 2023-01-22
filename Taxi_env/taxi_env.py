import gym

# Create the Taxi environment
env = gym.make("Taxi-v3")

# Reset the environment
observation = env.reset()

# Run the environment for 1000 timesteps
for _ in range(2000):
    # Render the environment
    env.render()

    # Select a random action
    action = env.action_space.sample()
    print('Action Taken ::  ', action)
    # Take the action and observe the result
    observation, reward, done, info = env.step(action)

    # Check if the episode is over
    if done:
        print("Episode finished after {} timesteps".format(_+1))
        break