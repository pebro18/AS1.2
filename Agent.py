import Maze
import Policy

class Agent:
    def __init__(self,maze,policy, start_state):
        self.maze = maze
        self.policy = policy
        self.state = start_state
        self.total_reward = 0

    def act(self):
        action = self.policy.select_action(self.maze.maze_states, self.state)
        self.state = self.maze.step(action, self.state)

    def value_function(self):

        """
        Pseudoalgoritme BEE:
        With sum(p,0) == 0
        For each following iteration i:
            For each part p:
                sum(p,i) = 0
                for each transition:
                    sum(p,i) += Chance of Transition * (Reward of next destination + Discount value * sum(p,i-1)
        """
        

        pass

    def print_position(self):
        print(f"Agent at: {self.state.position}")
