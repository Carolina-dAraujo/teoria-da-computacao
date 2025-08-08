from automata.afnd import AFND
from automata.afd import AFD

def determinizar(afnd: AFND) -> AFD:
    from collections import deque

    initial_closure = frozenset(afnd.epsilon_closure({afnd.initial_state}))
    queue = deque([initial_closure])
    visited = {initial_closure}
    transitions = {}
    state_names = {initial_closure: state_name(initial_closure)}
    final_states = set()
    all_states = set()

    while queue:
        current = queue.popleft()
        current_name = state_names[current]
        transitions[current_name] = {}
        all_states.add(current_name)

        for symbol in afnd.alphabet:
            if symbol == '': continue  # Ignorar ε
            next_states = set()
            for state in current:
                next_states.update(afnd.get_next_states(state, symbol))
            closure = frozenset(afnd.epsilon_closure(next_states))

            if not closure:
                continue
            if closure not in state_names:
                state_names[closure] = state_name(closure)
                visited.add(closure)
                queue.append(closure)
            transitions[current_name][symbol] = state_names[closure]

    for subset, name in state_names.items():
        if afnd.final_states.intersection(subset):
            final_states.add(name)

    return AFD(
        states=set(state_names.values()),
        alphabet=afnd.alphabet - {''},
        transitions=transitions,
        initial_state=state_names[initial_closure],
        final_states=final_states
    )

def state_name(state_set):
    """Gera um nome de estado determinístico baseado no conjunto original."""
    return "{" + ",".join(sorted(str(s) for s in state_set)) + "}"
