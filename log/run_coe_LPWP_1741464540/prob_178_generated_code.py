from scipy.optimize import linprog

def prob_178():
    c = [0, 1]  # Coefficients for the objective function (minimize y)
    A = [[1, 1], [-0.4, -1]]  # Coefficients for the inequality constraints
    b = [100, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])
    return res.fun