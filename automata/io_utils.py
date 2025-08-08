import json

def load_automaton_from_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_automaton_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
