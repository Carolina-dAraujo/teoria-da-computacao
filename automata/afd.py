class AFD:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions  # dict[state][symbol] = state
        self.initial_state = initial_state
        self.final_states = set(final_states)

    def to_dict(self):
        return {
            "states": list(self.states),
            "alphabet": list(self.alphabet),
            "transitions": self.transitions,
            "initial_state": self.initial_state,
            "final_states": list(self.final_states),
        }
