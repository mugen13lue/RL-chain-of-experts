from scipy.optimize import linprog

def prob_285(wide_trail, narrow_trail):
    """
    Args:
        wide_trail: an integer, the number of wide trails
        narrow_trail: an integer, the number of narrow trails
    Returns:
        obj: an integer, the total amount of garbage produced
    """
    obj = 6 * wide_trail + 3 * narrow_trail
    return obj

def optimize_trails():
    c = [6, 3]  # Coefficients of the objective function to minimize
    A = [[1, 0], [1, 1]]  # Coefficients of the constraints
    b = [3, 225]  # Right-hand side of the constraints
    bounds = [(0, 3), (0, None)]  # Bounds for the variables

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res

# Solve the optimization problem
result = optimize_trails()
print("Number of wide trails:", round(result.x[0]))
print("Number of narrow trails:", round(result.x[1]))
print("Total amount of garbage produced:", round(result.fun))