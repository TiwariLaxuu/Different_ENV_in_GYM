# Different_ENV_in_GYM

The environment consists of a 5x5 grid, where the agent (a taxi) is able to move in four cardinal directions (up, down, left, or right). There are four designated locations in the grid, which are labeled as “R”, “G”, “Y”, and “B”. Each state is represented by the tuple: (taxi_row, taxi_col, passenger_location, destination). Note that the passenger_location can also be in the taxi so that adds an extra 1 to the possible values that state component can take on. Furthermore, there are also six actions, corresponding to

0: move south
1: move north
2: move east
3: move west
4: pickup passenger
5: drop off passenger

