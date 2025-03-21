from scipy.optimize import linprog

def prob_135(sulfate, ginger, constraint1, constraint2, constraint3):
    c = [0.5, 0.75]  # Coefficients of the objective function
    A = [[-1, 0], [-1, -1], [-2, 1]]  # Coefficients of the constraints
    b = [-sulfate, -ginger, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    return res.fun