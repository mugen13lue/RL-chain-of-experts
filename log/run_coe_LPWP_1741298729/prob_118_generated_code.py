from scipy.optimize import linprog

def prob_118(vitamin_shots, pills, var1, var2, var3, var4, var5, var6):
    """
    Args:
        vitamin_shots: an integer, the number of batches of vitamin shots
        pills: an integer, the number of batches of vitamin pills
        var1: an integer, the number of units of vitamin C required for a batch of vitamin shots
        var2: an integer, the number of units of vitamin D required for a batch of vitamin shots
        var3: an integer, the number of units of vitamin C required for a batch of vitamin pills
        var4: an integer, the number of units of vitamin D required for a batch of vitamin pills
        var5: an integer, the maximum number of batches of vitamin shots
        var6: an integer, the number of people supplied by one batch of vitamin pills
    Returns:
        obj: an integer, the maximum number of people that can be supplied
    """
    c = [-10, -7]  # Coefficients of the objective function to maximize 10x + 7y

    A = [[var1, var3], [var2, var4], [-1, 0], [0, -1], [-1, 1]]  # Coefficients of the constraints for vitamin C and D, and additional constraints
    b = [var5, var6, 0, 0, 0]  # Right-hand side of the constraints

    bounds = [(0, None), (0, None)]  # Bounds for x (shots) and y (pills)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(-res.fun)  # Return the maximum number of people that can be supplied