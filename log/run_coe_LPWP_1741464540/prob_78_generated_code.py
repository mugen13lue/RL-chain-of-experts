from scipy.optimize import linprog

def prob_78(small, large, twice):
    """
    Args:
        small: an integer, representing the number of small crates
        large: an integer, representing the number of large crates
        twice: an integer, representing the requirement of large crates being twice the number of small crates

    Returns:
        obj: an integer, representing the objective value (number of crates produced)
    """
    c = [-1, -1]  # Coefficients for the objective function to maximize x + y
    A = [[20, 50], [-2, 1], [1, 0]]  # Coefficients for the constraints
    b = [500, 0, 5]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

    return int(-res.fun)