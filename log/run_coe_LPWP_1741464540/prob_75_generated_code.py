from scipy.optimize import linprog

def prob_75(traditional_machine, modern_machine):
    c = [-30, -40]  # Coefficients of the objective function to maximize 30x + 40y

    A = [[30, 40], [10, 15], [20, 15]]  # Coefficients of the constraints
    b = [500, 6000, 9000]  # RHS of the constraints

    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(-res.fun)  # Return the maximum amount of tea leaves that can be picked