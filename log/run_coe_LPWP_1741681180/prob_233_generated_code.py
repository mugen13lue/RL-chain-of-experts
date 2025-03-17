def prob_233(high_volume, low_volume):
    """
    Args:
        high_volume: an integer, number of high-volume pipes
        low_volume: an integer, number of low-volume pipes
    Returns:
        obj: an integer, objective value
    """
    
    from scipy.optimize import linprog

    c = [1, 1]  # Coefficients of the objective function to minimize x + y

    A = [[-10000, -5000],  # Demand Constraint: 10000x + 5000y >= 150000
         [12, 5],  # Technician Constraint: 12x + 5y <= 160
         [-0.65, 0.35],  # High-Volume Pipe Limit: x <= 0.35(x+y)
         [0, -1]]  # Low-Volume Pipe Minimum: y >= 8

    b = [-150000, 160, 0, -8]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b)

    obj = res.fun  # Objective value

    return obj