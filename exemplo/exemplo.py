from automata.io_utils import load_automaton_from_json, save_automaton_to_json
from automata.determination import determinizar
from automata.afnd import AFND

# 1. Carrega o AFND como dicionário
afnd_dict = load_automaton_from_json("exemplo/afnd_exemplo.json")

# 2. Converte para objeto da classe AFND
afnd = AFND.from_dict(afnd_dict)

print("\n=== AFND Original ===")
print(afnd.to_dict())

# 3. Determiniza
afd = determinizar(afnd)

print("\n=== AFD Determinizado ===")
print(afd.to_dict())

# 4. Salva resultado como JSON
save_automaton_to_json(afd.to_dict(), "exemplo/afd_resultado.json")
