from scipy.optimize import linprog

def prob_147(beam_bridges, truss_bridges):
    """
    Args:
        beam_bridges: an integer, representing the number of beam bridges
        truss_bridges: an integer, representing the number of truss bridges
        
    Returns:
        obj: an integer, representing the maximum total mass that can be supported
    """
    c = [-40, -60]  # Coefficients of the objective function to maximize total mass
    A = [[30, 50], [5, 8], [0, -1], [-1, 0], [-1, 0], [0, -1]]  # Coefficients of the inequality constraints
    b = [600, 100, -5, 0, 0, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, 5)]  # Bounds for the variables x (beam bridges) and y (truss bridges)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(-res.fun)  # Return the maximum total mass that can be supported