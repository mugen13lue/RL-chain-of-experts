from scipy.optimize import linprog

def prob_239():
    c = [1, 1]  # Coefficients of the objective function to minimize (x + y)
    A = [[-1, -1], [-0.7, -1]]  # Coefficients of the inequality constraints
    b = [-400, 0]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    limousine = round(res.x[0])
    bus = round(res.x[1])

    return limousine, bus