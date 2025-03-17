from scipy.optimize import linprog

def prob_182():
    c = [40, 30]  # Coefficients of the objective function to minimize total time
    A = [[30, 20], [-1, 0], [0, -1], [-0.6, -0.6]]  # Coefficients of the constraints
    b = [300, -5, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun