from scipy.optimize import linprog

def prob_17(chair, dresser, constraint1, constraint2):
    c = [-43, -52]  # Coefficients of the objective function to be minimized
    A = [[1.4, 1.1], [2, 3]]  # Coefficients of the constraints
    b = [constraint1, constraint2]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables (non-negativity constraint)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return -res.fun  # Return the maximum profit (negative of the minimized value)