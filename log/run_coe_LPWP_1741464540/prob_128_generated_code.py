from scipy.optimize import linprog

def prob_128(liquid_hand_sanitizer, foam_hand_sanitizer, water, alcohol, available_water, available_alcohol, liquid_constraint, foam_constraint):
    c = [-30, -20]  # Coefficients of the objective function to be minimized (-30x - 20y)
    A = [[40, 60], [50, 40], [-1, 0], [0, -1], [-1, 1]]  # Coefficients of the inequality constraints
    b = [available_water, available_alcohol, -liquid_constraint, -foam_constraint, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    max_hands_cleaned = -res.fun  # Maximum number of hands that can be cleaned

    return int(max_hands_cleaned)