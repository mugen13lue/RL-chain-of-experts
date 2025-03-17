from scipy.optimize import linprog

def prob_100(Pill_1, Pill_2):
    c = [0.3, 0.1]  # Coefficients of the objective function to minimize
    A = [[-0.2, -0.6], [0.3, 0.2]]  # Coefficients of the inequality constraints
    b = [-6, 3]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun