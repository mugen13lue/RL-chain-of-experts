from scipy.optimize import linprog

def prob_124():
    c = [-4, -5]  # Coefficients of the objective function to maximize 4x + 5y

    A = [[3, 2], [4, 5], [0, -1], [-3, 1]]  # Coefficients of the constraints
    b = [200, 0, -10, 0]  # Right-hand side of the constraints

    bounds = [(3, None), (10, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun * -1  # Return the maximum zinc intake