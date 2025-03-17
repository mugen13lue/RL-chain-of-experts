from scipy.optimize import linprog

def prob_277():
    c = [-1, -1]  # Coefficients of the objective function to maximize x + y
    A = [[5, -2], [2, -1], [0, -1], [5, 2], [2, 1]]  # Coefficients of the constraints
    b = [0, 0, -30, 1000, 250]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    return int(-res.fun)  # Maximum total number of keyboards manufactured