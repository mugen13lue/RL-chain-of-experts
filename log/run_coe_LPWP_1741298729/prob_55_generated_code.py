from scipy.optimize import linprog

def prob_55(windrower, hay_harvester):
    """
    Args:
        windrower: an integer,
        hay_harvester: an integer,
    Returns:
        windrower_acres: an integer,
        hay_harvester_acres: an integer,
    """
    c = [-10, -8]  # Coefficients of the objective function to minimize (-10x - 8y)
    A = [[10, 8], [5, 3], [2, 1]]  # Coefficients of the left-hand side of constraints
    b = [200, 800, 300]  # Right-hand side of constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negative)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    return int(res.x[0]), int(res.x[1])