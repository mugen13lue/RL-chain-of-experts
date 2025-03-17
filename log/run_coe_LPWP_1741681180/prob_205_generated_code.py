from scipy.optimize import linprog

def prob_205(protein_bars, noodles):
    """
    Minimize the cost of the diet.

    Args:
        protein_bars: an integer representing the number of protein bars.
        noodles: an integer representing the number of servings of noodles.

    Returns:
        obj: the objective value, i.e., the minimum cost of the diet.
    """
    # Coefficients of the objective function
    c = [5, 2.5]

    # Coefficients of the inequality constraints
    A = [[600, 250], [1.5, 5]]
    b = [2000, 16]

    # Bounds for variables x and y
    x_bounds = (0, None)
    y_bounds = (0, None)

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the minimum cost of the diet
    obj = res.fun

    return obj