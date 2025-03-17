from scipy.optimize import linprog

def prob_101(alpha, omega):
    c = [20, 15]  # Coefficients of the objective function (sugar intake)
    A = [[-30, -20], [-350, -300], [0, -1]]  # Coefficients of the inequality constraints
    b = [-100, -2000, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negative)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(res.fun)  # Return the minimized sugar intake