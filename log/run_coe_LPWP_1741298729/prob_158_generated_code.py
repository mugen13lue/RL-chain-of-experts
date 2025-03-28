from scipy.optimize import linprog

def prob_158():
    c = [1, 1]  # Coefficients of the objective function to minimize x + y
    A = [[-20, -50], [0, -1]]  # Coefficients of the inequality constraints
    b = [-500, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun