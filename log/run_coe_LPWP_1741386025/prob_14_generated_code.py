from scipy.optimize import linprog

def prob_14(long, short_cables, constraint1, constraint2, constraint3):
    """
    Args:
        long: an integer, the number of long cables
        short_cables: an integer, the number of short cables
        constraint1: an integer, the value of the first constraint
        constraint2: an integer, the value of the second constraint
        constraint3: an integer, the value of the third constraint

    Returns:
        obj: an integer, the objective value
    """
    c = [-12, -5]  # Coefficients of the objective function to be minimized (-12x - 5y)
    A = [[10, 7], [-5, -1], [-1, 0], [0, -1]]  # Coefficients of the left-hand side of constraints
    b = [constraint1, constraint2, -constraint3, 0]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(10, None))  # Solving the linear programming problem

    return -res.fun  # Returning the maximum profit value