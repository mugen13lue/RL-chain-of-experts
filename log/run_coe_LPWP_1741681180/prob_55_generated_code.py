from scipy.optimize import linprog

def prob_55(windrower, hay_harvester):
    c = [-10, -8]  # Coefficients of the objective function to minimize (-10x - 8y)
    A = [[1, 1], [2, 1], [5, 3]]  # Coefficients of the constraints
    b = [200, 300, 800]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun * -1  # Return the negative of the minimized objective function value