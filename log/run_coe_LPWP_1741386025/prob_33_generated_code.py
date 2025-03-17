from scipy.optimize import linprog

def prob_33(long_desks, short_desks):
    c = [-6, -2]  # Coefficients of the objective function to maximize (6x + 2y)
    A = [[300, 100], [10, 4]]  # Coefficients of the inequality constraints
    b = [2000, 200]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraints)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    objective_value = res.fun  # Maximize 6x + 2y
    return objective_value