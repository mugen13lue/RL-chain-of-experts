from scipy.optimize import linprog

def prob_286(wine, kombucha, _3, _8, _5, _7, _7000, _9000, _20_percent):
    c = [3, 5]  # Coefficients of the objective function to minimize (3x + 5y)
    A = [[3, 5], [8, 7], [-1, 1], [0, -0.2]]  # Coefficients of the constraints
    b = [9000, 7000, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun