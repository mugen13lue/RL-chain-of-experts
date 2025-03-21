from scipy.optimize import linprog

def prob_39():
    """
    Solves the ice cream production optimization problem using linear programming.

    Returns:
        int: The maximum profit that can be achieved.
    """
    objective_coefficients = [-200, -300]  # Coefficients of the objective function to maximize profit
    constraint_coefficients = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 2], [0, 2]]  # Coefficients of the constraints
    constraint_rhs = [10, 8, -5, -5, 30, 6]  # Right-hand side of the constraints

    res = linprog(c=objective_coefficients, A_ub=constraint_coefficients, b_ub=constraint_rhs, method='highs')
    max_profit = -res.fun  # Maximum profit is the negative of the minimum value found by linprog

    return int(max_profit)