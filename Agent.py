from Actions import Actions


class Agent:
    def __init__(self, maze, policy, start_state):
        self.maze = maze
        self.state = start_state
        self.total_reward = 0

        self.policy = policy
        self.threshold = 0.01

    def act(self):
        possible_states = []
        for action in Actions:
            possible_states.append(
                (self.maze.step(action, self.state), 0, action))
        best_action = self.value_function(possible_states)
        self.state = best_action[0]
        self.policy.policy[self.state.position[0]
                           ][self.state.position[1]] = best_action[1]
        self.total_reward += self.state.reward

    def value_function(self, possible_states):

        # initialize V(s) arbitrarily
        # repeat
        #     delta = 0
        #     for each s in S:
        #         v = V(s)
        #         V(s) = max_a(sum_s'(T(s,a,s') * (R(s,a,s') + gamma * V(s'))))
        #         delta = max(delta, |v - V(s)|)
        # until delta < theta

        while True:
            delta = 0

            for index, state in enumerate(possible_states):
                v = state[1]
                action = self.policy.select_action(possible_states)
                possible_states[index] = action
                delta = max(delta, abs(v - action[1]))
            if delta < self.threshold:
                break

        return max(possible_states, key=lambda x: x[1])

    def print_position(self):
        print(f"Agent at: {self.state.position}")
