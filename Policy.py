
import random
from Actions import Actions
class Policy:
    def __init__(self, discount_factor = 0.9):
        self.policy = None
        self.discount_factor = discount_factor

    def select_action(self, state, position_state):
        number = random.randrange(0,4)
        return Actions(number)
    
    def value_iteration(self , states):

        # initialize V(s) arbitrarily       
        # repeat
        #     delta = 0
        #     for each s in S:
        #         v = V(s)
        #         V(s) = max_a(sum_s'(T(s,a,s') * (R(s,a,s') + gamma * V(s'))))
        #         delta = max(delta, |v - V(s)|)
        # until delta < theta


        threshold = 0.01

        self.policy = None