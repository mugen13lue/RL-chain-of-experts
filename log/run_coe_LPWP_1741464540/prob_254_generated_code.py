from scipy.optimize import linprog

def prob_254():
    c = [-25, -6]  # Coefficients of the objective function to be maximized (-25x - 6y)
    A = [[4, 1.5], [-1, 2], [0, -1]]  # Coefficients of the inequality constraints
    b = [110, 0, -20]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    max_grain_weight = -res.fun  # Maximum amount of grain in weight

    return int(max_grain_weight)