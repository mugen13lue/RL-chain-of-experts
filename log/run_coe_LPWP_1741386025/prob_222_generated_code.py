from scipy.optimize import linprog

def prob_222(strawberry_cookie, sugar_cookie):
    c = [-5.5, -12]  # Coefficients of the objective function to maximize (5.5x1 + 12x2)
    A = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1]]  # Coefficients of the inequality constraints
    b = [100, 80, 0, 0, 100]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    max_profit = res.fun  # Maximum profit obtained by linprog

    return -max_profit