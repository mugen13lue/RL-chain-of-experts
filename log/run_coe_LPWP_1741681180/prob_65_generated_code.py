from scipy.optimize import linprog

def prob_65(small_oil_well, large_oil_well):
    """
    Args:
        small_oil_well: an integer, number of acres to be used for small oil wells
        large_oil_well: an integer, number of acres to be used for large oil wells

    Returns:
        Total_Production_of_Oil: an integer, total production of oil
    """
    # Coefficients of the objective function to maximize total production of oil
    c = [-2, -5]

    # Coefficients of the inequality constraints
    A = [[5, 10], [10, 20]]
    b = [2500, 4500]

    # Bounds for the variables x and y (number of acres for small and large oil wells)
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal values of x and y
    optimal_acres_small_oil_well = res.x[0]
    optimal_acres_large_oil_well = res.x[1]

    # Calculate the total production of oil based on the optimal acres
    total_production = 2 * optimal_acres_small_oil_well + 5 * optimal_acres_large_oil_well

    return total_production

# No test code needed here

# The final code uses linear programming to find the optimal number of acres for small and large oil wells
# in order to maximize the total production of oil