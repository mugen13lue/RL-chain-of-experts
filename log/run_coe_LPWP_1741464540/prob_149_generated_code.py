from scipy.optimize import linprog

def prob_149():
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y
    A = [[-50, -80], [-30, -50], [-1, 1]]  # Coefficients of the inequality constraints
    b = [-1500, -1000, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])

    return res.fun