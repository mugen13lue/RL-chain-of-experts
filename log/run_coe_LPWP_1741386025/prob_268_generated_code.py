from scipy.optimize import linprog

def prob_268(in_vivo, ex_vivo, constraint1, constraint2):
    c = [2, 3]  # Coefficients of the objective function (2x + 3y)
    A = [[30, 45], [60, 30]]  # Coefficients of the constraints
    b = [constraint1, constraint2]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun