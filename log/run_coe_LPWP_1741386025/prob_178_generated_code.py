from scipy.optimize import linprog

def prob_178():
    c = [0, 1]  # Coefficients for the objective function (minimize y)
    A = [[-5, -3], [-1, -1], [-0.4, 1]]  # Coefficients for the constraints
    b = [-500, -100, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    return res.fun