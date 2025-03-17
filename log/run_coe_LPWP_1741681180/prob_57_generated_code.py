from scipy.optimize import linprog

def prob_57(cash_based, card_only):
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[-20, -30], [4, 5], [-1, 1]]  # Coefficients for the inequality constraints
    b = [-500, 90, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.x[0]), int(res.x[1])