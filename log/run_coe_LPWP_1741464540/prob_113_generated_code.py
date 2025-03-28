from scipy.optimize import linprog

def prob_113(children_vaccines, adult_vaccines):
    c = [50, 75]  # Coefficients of the objective function (fever suppressant)
    A = [[50, 75], [-1, -1], [-0.3, 0.3]]  # Coefficients of the constraints
    b = [20000, -50, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(50, None), (0, None)])

    return res.fun