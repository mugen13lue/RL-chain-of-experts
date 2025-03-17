from scipy.optimize import linprog

def prob_111(crab_cakes, lobster_roll, constraint1, constraint2, constraint3, constraint4, constraint5, constraint6):
    """
    Args:
        crab_cakes: an integer, representing the number of crab cakes to eat
        lobster_roll: an integer, representing the number of lobster rolls to eat
        constraint1: an integer, representing the first constraint threshold
        constraint2: an integer, representing the second constraint threshold
        constraint3: an integer, representing the third constraint threshold
        constraint4: an integer, representing the fourth constraint threshold
        constraint5: an integer, representing the fifth constraint threshold
        constraint6: an integer, representing the sixth constraint threshold
    Returns:
        obj: an integer, representing the minimized unsaturated fat intake
    """
    c = [4, 6]  # Coefficients of the objective function to minimize unsaturated fat intake
    A = [[-5, -8], [-7, -4], [0, -1], [1, 1]]  # Coefficients of the constraints
    b = [-constraint1, -constraint2, -constraint3, 0]  # Right-hand side of the constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun