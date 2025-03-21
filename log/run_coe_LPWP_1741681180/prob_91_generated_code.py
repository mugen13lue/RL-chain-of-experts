from scipy.optimize import linprog

def prob_91(A, B, _30, _100, _50, _120):
    c = [1, 1]  # Coefficients for the objective function to minimize total number of machines
    A_ub = [[-A, -B], [0, -1], [0, 1]]  # Coefficients for the inequality constraints
    b_ub = [-_30, -_100, _120]  # Right-hand side of the inequality constraints
    bounds = [(5, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    obj = int(res.fun)  # Minimum total number of machines

    return obj