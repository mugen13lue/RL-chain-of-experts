from scipy.optimize import linprog

def prob_276(spinach, soybeans):
    """
    Args:
        spinach: an integer, number of cups of spinach
        soybeans: an integer, number of cups of soybeans
    Returns:
        obj: an integer, the maximum caloric intake
    """
    
    objective_coefficients = [-30, -100]  # Coefficients of the objective function to minimize (-30x - 100y)
    constraint_coefficients = [[-1, 1], [-100, -80], [-5, -12]]  # Coefficients of the inequality constraints
    constraint_bounds = [0, -12000, -300]  # Right-hand side of the inequality constraints

    res = linprog(objective_coefficients, A_ub=constraint_coefficients, b_ub=constraint_bounds, bounds=(0, None))

    return int(-res.fun)  # Return the maximum caloric intake (negate the result to maximize)