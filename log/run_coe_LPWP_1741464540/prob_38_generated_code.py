from scipy.optimize import linprog

def prob_38(A, B):
    """
    Args:
        A: an integer, number of cups of drink A
        B: an integer, number of cups of drink B
    Returns:
        obj: an integer, value of the objective function
    """
    c = [4, 12]  # Coefficients of the objective function to minimize 4x + 12y
    A_ub = [[-8, -15], [-6, -2], [10, 20]]  # Coefficients of the inequality constraints
    b_ub = [-150, -300, 400]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

    return res.fun