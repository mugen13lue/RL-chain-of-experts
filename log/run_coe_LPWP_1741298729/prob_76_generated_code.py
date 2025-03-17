from scipy.optimize import linprog

def prob_76(light_grilled_cheese_sandwiches, heavy_grilled_cheese_sandwiches):
    """
    Args:
        light_grilled_cheese_sandwiches: an integer, the number of light grilled cheese sandwiches
        heavy_grilled_cheese_sandwiches: an integer, the number of heavy grilled cheese sandwiches
    Returns:
        total_production_time: an integer, the total production time
    """
    c = [10, 15]  # Coefficients of the objective function to minimize total production time
    A = [[2, 3], [3, 5], [-3, 1]]  # Coefficients of the constraints
    b = [300, 500, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    total_production_time = res.fun
    return total_production_time