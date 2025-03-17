def prob_176(small, large):
    """
    Args:
        small: an integer, number of small jars
        large: an integer, number of large jars
    Returns:
        obj: an integer, the objective value
    """
    obj = 1e9
    
    # Define the optimization problem
    from scipy.optimize import linprog

    c = [1, 1]  # Coefficients of the objective function to minimize x + y
    A = [[50, 200], [-1, 1]]  # Coefficients of the constraints
    b = [100000, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)
    
    if res.success:
        obj = int(res.fun)  # Minimum number of jars
    else:
        print("Optimization failed.")

    return obj