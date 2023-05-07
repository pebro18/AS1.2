from email import policy


class Policy:
    def __init__(self, discount_factor=0.1, lenght=4, width=4):
        self.policy = [[0 for i in range(lenght)] for j in range(width)]
        self.discount_factor = discount_factor

    def select_action(self, states):

        states = list(states)
        for index, state in enumerate(states):
            calculation = state[0].reward + self.discount_factor * \
                self.policy[state[0].position[0]][state[0].position[1]]
            states[index] = tuple((state[0], calculation, state[2]))
        chosen_action = max(states, key=lambda x: x[1])
        return chosen_action

    def calculate_value(self, value_state):
        if value_state[0].terminal:
            return value_state[0].reward
        return value_state[0].reward + self.discount_factor * value_state[1]
