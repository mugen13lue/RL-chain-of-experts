from scipy.optimize import linprog

def prob_122(cheap_box, expensive_box, constraint1, constraint2, constraint3):
    """
    Solve a linear programming problem to maximize the amount of foam produced.

    Args:
        cheap_box: an integer, the number of cheap boxes to make
        expensive_box: an integer, the number of expensive boxes to make
        constraint1: a list of three integers [3, 5, 200], representing the metal constraint
        constraint2: a list of three integers [5, 8, 300], representing the acid constraint
        constraint3: a list of three integers [2, 3, 50], representing the heat constraint

    Returns:
        obj: an integer, the maximum amount of foam produced
    """
    c = [-8, -10]  # Coefficients of the objective function to maximize 8x + 10y

    A = [[3, 5], [5, 8], [2, 3]]  # Coefficients of the constraints
    b = [200, 300, 50]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return -res.fun  # Return the negative of the optimized objective function value