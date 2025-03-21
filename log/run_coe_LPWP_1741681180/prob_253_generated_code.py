from scipy.optimize import linprog

def prob_253(small_boxes, large_boxes):
    """
    Solves the Box Packing problem.

    Args:
        small_boxes: an integer, representing the number of small boxes to be used.
        large_boxes: an integer, representing the number of large boxes to be used.

    Returns:
        obj: an integer, representing the objective value (minimize the total number of boxes needed).
    """
    # Define the coefficients of the objective function
    c = [1, 1]

    # Define the coefficients of the inequality constraints
    A = [[-1, 3], [0, -1], [-25, -45]]
    b = [-5, -750]

    # Define the bounds for x and y (number of small and large boxes)
    x_bounds = (0, None)
    y_bounds = (5, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    x_opt = res.x[0]
    y_opt = res.x[1]

    # Return the total number of boxes used as the objective value
    return int(x_opt + y_opt)