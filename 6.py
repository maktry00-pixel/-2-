# 4-тапсырма: Бағалау функциясы (Evaluation function)
def eval_state(margin, reliability, capacity, w):
    return w[0] * margin + w[1] * reliability + w[2] * capacity

# Күйлер: (Margin, Reliability, Capacity)
state_x = (8, 7, 2)
state_y = (5, 5, 8)

# A нұсқасы (бастапқы салмақтар)
w_initial = (0.5, 0.3, 0.2)
ev_x1 = eval_state(*state_x, w_initial)
ev_y1 = eval_state(*state_y, w_initial)
print(f"Бастапқы: X-Y = {ev_x1 - ev_y1:.4f}; Таңдау = {'X' if ev_x1 > ev_y1 else 'Y'}")

# B нұсқасы (өзгертілген салмақтар)
w_new = (0.3125, 0.1875, 0.5)
ev_x2 = eval_state(*state_x, w_new)
ev_y2 = eval_state(*state_y, w_new)
print(f"Жаңа салмақпен: X-Y = {ev_x2 - ev_y2:.4f}; Таңдау = {'X' if ev_x2 > ev_y2 else 'Y'}")

# Expectimax есебі (24-слайд)
payoffs_game = {
    "A": (8, 6, 4),
    "B": (3, 7, 5),
    "C": (2, 9, 1)
}
probs = {
    "A": (0.2, 0.3, 0.5),
    "B": (0.2, 0.5, 0.3),
    "C": (0.7, 0.2, 0.1)
}

print("\nExpectimax мәндері:")
for strat in ("A", "B", "C"):
    exp_val = sum(p * v for p, v in zip(probs[strat], payoffs_game[strat]))
    print(f"E({strat}) = {exp_val:.2f}")