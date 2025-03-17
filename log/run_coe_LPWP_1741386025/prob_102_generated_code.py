from scipy.optimize import linprog

def prob_102(beaker_1, beaker_2, constraint1, constraint2, constraint3, constraint4, constraint5, constraint6):
    """
    Args:
        beaker_1: an integer, number of units of flour used by beaker 1
        beaker_2: an integer, number of units of flour used by beaker 2
        constraint1: an integer, limit on total units of flour available
        constraint2: an integer, limit on total units of special liquid available
        constraint3: an integer, limit on total units of waste produced
        constraint4: an integer, limit on units of waste produced by beaker 1
        constraint5: an integer, limit on units of waste produced by beaker 2
        constraint6: an integer, limit on units of slime produced by beaker 1

    Returns:
        amount_of_slime: an integer, maximum amount of slime that can be produced
    """
    c = [-5, -3]  # Coefficients of the objective function to be minimized (-5x - 3y)
    A = [[4, 6], [6, 3], [4, 2]]  # Coefficients of the inequality constraints
    b = [constraint1, constraint2, constraint3]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for x and y (non-negativity constraints)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    amount_of_slime = -res.fun  # Maximum amount of slime produced

    return int(amount_of_slime)