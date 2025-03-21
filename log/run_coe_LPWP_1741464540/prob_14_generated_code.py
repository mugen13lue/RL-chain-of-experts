from scipy.optimize import linprog

def prob_14(long, short_cables, constraint1, constraint2, constraint3):
    """
    Args:
        long: an integer, the number of long cables
        short_cables: an integer, the number of short cables
        constraint1: an integer, the total amount of gold available
        constraint2: an integer, the relationship constraint between long and short cables
        constraint3: an integer, the minimum number of long cables to be made

    Returns:
        obj: an integer, the objective value (maximum profit)
    """
    
    # Coefficients of the objective function to maximize profit
    c = [-12, -5]  # Coefficients for x (long cables) and y (short cables)

    # Coefficients of the inequality constraints
    A = [[10, 7], [-5, 1], [-1, 0], [0, -1]]  # Coefficients for the constraints
    b = [constraint1, constraint2, -constraint3, 0]  # RHS of the constraints

    # Bounds for the variables
    x_bounds = (10, None)  # At least 10 long cables
    y_bounds = (0, None)  # Non-negativity constraint for short cables

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    return -res.fun  # Return the negative of the objective value as linprog minimizes by default