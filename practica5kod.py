GRID = (("A", "B", "C", "G"),
        ("D", "#", "E", "X"),
        ("S", "F", "H", "I"))
TERMINALS = {"G", "X"}
ACTIONS = ("UP", "DOWN", "LEFT", "RIGHT")
MOVES = {"UP": (-1, 0), "DOWN": (1, 0),
         "LEFT": (0, -1), "RIGHT": (0, 1)}
SIDES = {"UP": ("LEFT", "RIGHT"),
         "DOWN": ("RIGHT", "LEFT"),
         "LEFT": ("DOWN", "UP"),
         "RIGHT": ("UP", "DOWN")}
gamma, theta = 0.9, 0.001
probs = defaultdict(float)
directions = (a,) + SIDES[a]
weights = (p_main, (1-p_main)/2, (1-p_main)/2)
r, c = POS[s]
for direction, p in zip(directions, weights):
    dr, dc = MOVES[direction]
    nr, nc = r+dr, c+dc
    valid = 0 <= nr < 3 and 0 <= nc < 4 and GRID[nr][nc] != "#"
    nxt = GRID[nr][nc] if valid else s
    probs[nxt] += p
return [(p, nxt, 10.0 if nxt == "G" else
         danger if nxt == "X" else step)
        for nxt, p in probs.items() if p > 0]
def q_value(s, a, V):
    return sum(p * (r + gamma * V.get(nxt, 0.0))
               for p, nxt, r in transitions(s, a))

V = {s: 0.0 for s in POS}
while True:
    new_V = V.copy()
    for s in STATES:
        new_V[s] = max(q_value(s, a, V) for a in ACTIONS)
    delta = max(abs(new_V[s] - V[s]) for s in STATES)
    V = new_V
    if delta < theta:
        break
policy = {s: max(ACTIONS, key=lambda a: q_value(s, a, V))
          for s in STATES}

