class AFND:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions  # dict[state][symbol] = set(states)
        self.initial_state = initial_state
        self.final_states = set(final_states)

    def get_next_states(self, state, symbol):
        return self.transitions.get(state, {}).get(symbol, set())

    def epsilon_closure(self, states):
        """Computa o fecho-ε de um conjunto de estados."""
        stack = list(states)
        closure = set(states)

        while stack:
            state = stack.pop()
            for next_state in self.get_next_states(state, ''):  # '' representa transição ε
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    @staticmethod
    def from_dict(data):
        # Converte listas para sets, se necessário
        transitions = {}
        for state, symbol_dict in data["transitions"].items():
            transitions[state] = {}
            for symbol, targets in symbol_dict.items():
                transitions[state][symbol] = set(targets)

        return AFND(
            states=data["states"],
            alphabet=data["alphabet"],
            transitions=transitions,
            initial_state=data["start_state"],
            final_states=data["accept_states"]
        )

    def to_dict(self):
        # Converte sets de volta para listas para serializar em JSON
        transitions = {}
        for state, symbol_dict in self.transitions.items():
            transitions[state] = {}
            for symbol, targets in symbol_dict.items():
                transitions[state][symbol] = list(targets)

        return {
            "type": "AFND",
            "states": list(self.states),
            "alphabet": list(self.alphabet),
            "start_state": self.initial_state,
            "accept_states": list(self.final_states),
            "transitions": transitions
        }