class Maze:
    def __init__(self, length = 4, width = 4):
        self.maze = [[-1 for i in range(length)] for j in range(width)]

    def set_reward(self, state, reward):
        self.maze[state[0]][state[1]] = reward

    def step(self, action):
        pass        