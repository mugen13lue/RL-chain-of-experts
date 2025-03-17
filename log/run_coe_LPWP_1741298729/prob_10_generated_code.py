from scipy.optimize import linprog

def prob_10(A, B, constraint1, constraint2, constraint3):
    c = [5, 9]  # Coefficients of the objective function to minimize 5x + 9y

    A_eq = None  # No equality constraints
    b_eq = None

    A_ub = [[-13, -8], [-5, -14], [6, 6]]  # Coefficients of the inequality constraints
    b_ub = [-constraint1, -constraint2, constraint3]  # RHS of the inequality constraints

    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraints)

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    return res.fun  # Minimum amount of vitamin D