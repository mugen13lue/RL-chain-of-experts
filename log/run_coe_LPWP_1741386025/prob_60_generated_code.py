from scipy.optimize import linprog

def prob_60():
    c = [1, 1]  # Coefficients of the objective function to minimize total number of snow removers (x + y)

    A = [[-6, -10], [120, 250]]  # Coefficients of the inequality constraints
    b = [-300, 6500]  # Right-hand side of the inequality constraints

    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraint)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun  # Return the minimized total number of snow removers