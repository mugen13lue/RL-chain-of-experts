from scipy.optimize import linprog

def prob_46():
    c = [3, 5]  # Cost coefficients for vegetables and fruits
    A = [[-2, -4], [-3, -1]]  # Coefficients of constraints for vitamins and minerals
    b = [-20, -30]  # RHS of constraints
    bounds = [(0, None), (0, None)]  # Non-negativity bounds for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun