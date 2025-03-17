from scipy.optimize import linprog

def prob_146(blueberries, strawberries):
    """
    Args:
        blueberries: an integer, the number of packs of blueberries
        strawberries: an integer, the number of packs of strawberries
    Returns:
        sugar_intake: an integer, the minimum sugar intake
    """
    objective_coefficients = [5, 7]  # Coefficients of the objective function (sugar intake)
    constraint_coefficients = [[3, 1], [5, 7], [-3, 1], [-1, 0], [0, -1]]  # Coefficients of the inequality constraints
    constraint_constants = [90, 100, 0, 0, 0]  # Right-hand side of the inequality constraints

    res = linprog(c=objective_coefficients, A_ub=constraint_coefficients, b_ub=constraint_constants)
    sugar_intake = res.fun  # Minimum sugar intake

    return sugar_intake