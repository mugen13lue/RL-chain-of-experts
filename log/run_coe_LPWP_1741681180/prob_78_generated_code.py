from scipy.optimize import linprog

def prob_78(small, large, twice):
    """
    Args:
        small: an integer, representing the number of small crates
        large: an integer, representing the number of large crates
        twice: an integer, representing the requirement of large crates being twice the number of small crates

    Returns:
        obj: an integer, representing the objective value (number of crates produced)
    """
    
    # Coefficients of the objective function
    c = [-1, -1]

    # Coefficients of the inequality constraints
    A = [[20, 50], [-1, 2], [1, 0], [0, 1]]
    b = [500, 0, 0, 0]

    # Bounds for variables x and y
    x_bounds = (5, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    x_opt = int(res.x[0])
    y_opt = int(res.x[1])

    # Calculate the total number of crates produced
    total_crates = x_opt + y_opt

    return total_crates