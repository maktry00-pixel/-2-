
# 3-тапсырма. Деректер және ойын ағашы


# Ойын ағашының құрылымы
tree = {
    "A": ("B", "C"), 
    "B": ("D", "E"), 
    "C": ("F", "G"),
    "D": ("H", "I"), 
    "E": ("J", "K"),
    "F": ("L", "M"), 
    "G": ("N", "O"),
}

# Жапырақ түйіндердің ұтыс мәндері (payoffs)
payoffs = dict(zip("HIJKLMNO", (4, 9, 7, 2, 3, 8, 6, 1)))

def is_terminal(state):
    """Түйіннің соңғы (жапырақ) екенін тексереді"""
    return state in payoffs

def successors(state, reverse=False):
    """Түйіннің балаларын қайтарады (reverse=True болса, оңнан солға қарай)"""
    return tree[state][::-1] if reverse else tree[state]

def utility(state):
    """Жапырақ түйіннің пайдасын қайтарады"""
    return payoffs[state]

def new_counter():
    """Іздеу статистикасын тіркеуге арналған есептегіш"""
    return {"calls": 0, "visited": [], "pruned": [], "trace": []}



# Minimax алгоритмі

def minimax(state, maximizing, counter, reverse=False):
    counter["calls"] += 1
    counter["visited"].append(state)
    
    if is_terminal(state):
        return utility(state)
    
    scores = [
        minimax(child, not maximizing, counter, reverse)
        for child in successors(state, reverse)
    ]
    choose = max if maximizing else min
    return choose(scores)



# Alpha–Beta Pruning алгоритмі


def alphabeta(state, alpha, beta, maximizing, counter, reverse=False):
    counter["calls"] += 1
    counter["visited"].append(state)
    
    if is_terminal(state):
        return utility(state)
    
    row = {
        "node": state, 
        "alpha": alpha, 
        "beta": beta,
        "type": "MAX" if maximizing else "MIN",
        "children": [], 
        "pruned": []
    }
    counter["trace"].append(row)
    
    best = float("-inf") if maximizing else float("inf")
    choose = max if maximizing else min
    children = successors(state, reverse)

    for index, child in enumerate(children):
        score = alphabeta(child, alpha, beta, not maximizing, counter, reverse)
        row["children"].append(child)
        best = choose(best, score)
        
        if maximizing:
            alpha = max(alpha, best)
        else:
            beta = min(beta, best)
            
        # Қию шарты (Alpha-Beta cutoff)
        if alpha >= beta:
            row["pruned"] = list(children[index + 1:])
            counter["pruned"].extend(row["pruned"])
            break
            
    row["value"] = best
    return best



# Эксперименттерді орындау және салыстыру

def run_experiment(reverse):
    mm, ab = new_counter(), new_counter()
    m = minimax("A", True, mm, reverse)
    a = alphabeta("A", float("-inf"), float("inf"), True, ab, reverse)
    assert m == a, "Minimax және Alpha-Beta нәтижелері сәйкес келуі тиіс"
    return m, a, mm, ab

def main():
    for reverse in (False, True):
        m, a, mm, ab = run_experiment(reverse)
        print("RIGHT TO LEFT" if reverse else "LEFT TO RIGHT")
        print(f"Minimax: value={m}, calls={mm['calls']}")
        print(f"Alpha-Beta: value={a}, calls={ab['calls']}")
        print("Visited:", " ".join(ab["visited"]))
        print("Pruned:", ", ".join(ab["pruned"]) or "none")
        print()

if __name__ == "__main__":
    main()