from scipy.optimize import linprog

def prob_112(demonstration_1, demonstration_2, _10, _20, _25, _12, _15, _18, _5, _3, _120, _100, _50):
    c = [-25, -18]  # Coefficients of the objective function to be minimized

    A = [[10, 12], [20, 15], [5, 3]]  # Coefficients of the left-hand side of inequalities
    b = [120, 100, 50]  # Right-hand side of inequalities

    bounds = [(0, None), (0, None)]  # Bounds for the variables

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return -res.fun  # Return the negative of the objective value as linprog minimizes by default