from scipy.optimize import linprog

def prob_137(oranges, grapefruit):
    """
    Args:
        oranges: an integer, the number of oranges to eat
        grapefruit: an integer, the number of grapefruit to eat
    Returns:
        obj: an integer, the minimum sugar intake
    """
    
    # Coefficients of the objective function
    c = [5, 6]

    # Coefficients of the inequality constraints
    A = [[-5, -7], [-3, -5], [-1, 0]]
    b = [-80, -70, 0]

    # Bounds for variables x and y
    x_bounds = (2, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    x_opt = res.x[0]
    y_opt = res.x[1]

    # Calculate the minimum sugar intake
    min_sugar_intake = c[0]*x_opt + c[1]*y_opt

    return min_sugar_intake