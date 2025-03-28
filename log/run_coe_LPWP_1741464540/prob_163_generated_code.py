from scipy.optimize import linprog

def prob_163():
    c = [5, 10]  # Coefficients of the objective function to minimize 5x + 10y
    A = [[3, 7], [0, 1]]  # Coefficients of the constraints
    b = [80, 8]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    obj = res.fun  # The minimum amount of pollution produced

    return obj