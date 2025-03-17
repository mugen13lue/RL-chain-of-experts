from scipy.optimize import linprog

def prob_96(milk_chocolate_bars, dark_chocolate_bars):
    """
    Args:
        milk_chocolate_bars: an integer, representing the number of milk chocolate bars
        dark_chocolate_bars: an integer, representing the number of dark chocolate bars
    Returns:
        total_production_time: an integer, representing the total production time
    """
    c = [15, 12]  # Coefficients of the objective function to minimize
    A = [[4, 6], [7, 3], [-1, 2]]  # Coefficients of the left-hand side of constraints
    b = [2000, 1750, 0]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    if res.success:
        total_production_time = res.fun
        return total_production_time
    else:
        return "Optimization failed"