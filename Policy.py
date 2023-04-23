class Policy:
    def __init__(self):
        self.policy = {}

    def select_action(self, state):
        return self.policy[state]