from scipy.optimize import linprog

def prob_24():
    """
    Returns:
        obj: an integer, the objective value of the problem
    """
    c = [-30, -15]  # Coefficients of the objective function to maximize profit

    A = [[4, 2], [3, 1], [5, 2], [-1, 0], [0, -1]]  # Coefficients of the constraints
    b = [100, 50, 70, -5, -5]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')  # Using linear programming to maximize profit

    return res.fun  # Return the optimal profit value