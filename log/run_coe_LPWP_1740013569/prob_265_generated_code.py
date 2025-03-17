from scipy.optimize import linprog

def prob_265():
    c = [1, 1]  # Coefficients of the objective function to minimize Z = x + y

    A = [[-1, -1], [-0.6, -1]]  # Coefficients of the inequality constraints
    b = [-80, 0]  # Right-hand side of the inequality constraints

    bounds = [(0, None), (0, None)]  # Bounds for the decision variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun