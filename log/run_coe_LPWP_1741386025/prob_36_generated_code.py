from scipy.optimize import linprog

def prob_36(Oil_Max, Oil_Max_Pro, Constraint_A, Constraint_B, Constraint_C):
    """
    Args:
        Oil_Max: an integer, number of containers of Oil Max
        Oil_Max_Pro: an integer, number of containers of Oil Max Pro
        Constraint_A: an integer, value of constraint A
        Constraint_B: an integer, value of constraint B
        Constraint_C: an integer, value of constraint C

    Returns:
        Oil_Max: an integer, number of containers of Oil Max
        Oil_Max_Pro: an integer, number of containers of Oil Max Pro
        max_profit: an integer, maximum profit
    """
    c = [-10, -15]  # Coefficients of the objective function to minimize (-10x - 15y)
    A = [[46, 13], [43, 4], [56, 45]]  # Coefficients of the constraints
    b = [Constraint_A, Constraint_B, Constraint_C]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraint)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    max_profit = -res.fun  # Maximum profit is the negative of the minimum value obtained by linprog

    return int(res.x[0]), int(res.x[1]), max_profit