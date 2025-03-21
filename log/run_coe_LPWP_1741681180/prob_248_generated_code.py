from scipy.optimize import linprog

def prob_248(salad, fruit_bowl):
    """
    Find the maximum potassium intake for a navy ship's staff.

    Args:
        salad: An integer representing the number of salads prepared.
        fruit_bowl: An integer representing the number of fruit bowls prepared.

    Returns:
        objective_value: An integer representing the maximum potassium intake.
    """
    c = [-2, -8]  # Coefficients for the objective function to maximize potassium intake
    A = [[7, 15], [12, 3]]  # Coefficients for the constraints (vitamin and fibre)
    b = [90, 110]  # RHS of the constraints
    bounds = [(0, None), (0, 0.3 * salad)]  # Bounds for the number of salads and fruit bowls

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return -res.fun  # Return the negative of the objective function value as linprog minimizes by default