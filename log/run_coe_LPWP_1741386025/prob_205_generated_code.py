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
    c = [5, 2.5]  # Cost of noodles and protein bars
    A = [[600, 250], [1.5, 5]]  # Coefficients of the constraints
    b = [2000, 16]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun