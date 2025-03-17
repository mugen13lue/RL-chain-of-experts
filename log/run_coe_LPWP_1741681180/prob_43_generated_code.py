from scipy.optimize import linprog

def prob_43(Kebabs, Rice):
    c = [3, 2]  # Cost coefficients
    A = [[300, 200], [4.5, 4]]  # Coefficients of constraints
    b = [2200, 30]  # Right-hand side of constraints
    bounds = [(0, None), (0, None)]  # Non-negativity constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun