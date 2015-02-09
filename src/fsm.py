# coding; utf-8


class Fsm(object):

    def __init__(self, active_state, states=None):
        self.moves_count = 0
        self.side = "right"
        self.attack_count = 0
        self.states = states
        self.active_state = active_state

    def set_state(self, state):
        self.active_state = state

    def get_state(self):
        return self.active_state

    def auto_update(self):
        if self.active_state != "move":
            self.states[self.active_state]()

    def update(self, side):
        self.side = side
        self.moves_count += 1
        if self.moves_count == 8:
            self.moves_count = 0
        self.states[self.active_state]()
