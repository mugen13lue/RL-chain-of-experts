from scipy.optimize import linprog

def prob_167(small_wagons, large_wagons, twice):
    """
    Args:
        small_wagons: an integer, number of small wagons
        large_wagons: an integer, number of large wagons
        twice: an integer, twice the number of large wagons
    Returns:
        obj: an integer, number of wagons
    """
    # Coefficients of the objective function
    c = [1, 1]

    # Coefficients of the inequality constraints
    A = [[20, 50], [-1, 2], [0, -1]]
    b = [2000, 0, -10]

    # Bounds for variables
    x_bounds = (0, None)
    y_bounds = (10, None)

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    total_wagons = res.x[0] + res.x[1]
    return total_wagons