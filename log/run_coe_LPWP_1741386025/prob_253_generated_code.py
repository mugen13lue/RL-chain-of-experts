from scipy.optimize import linprog

def prob_253():
    c = [1, 1]  # Coefficients of the objective function to minimize x + y

    A = [[-1, 3], [0, -1], [-25, -45]]  # Coefficients of the inequality constraints
    b = [-5, -750]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun