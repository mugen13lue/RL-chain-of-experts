from scipy.optimize import linprog

def prob_150(small_bottles, large_bottles):
    """
    Args:
        small_bottles: an integer, the number of small bottles
        large_bottles: an integer, the number of large bottles
        
    Returns:
        amount_of_honey: an integer, the maximum amount of honey that can be transported
    """
    c = [-5, -20]  # Coefficients of the objective function to maximize 5x + 20y
    A = [[1, 0], [0, 1], [-2, 1], [1, 1], [0, -1]]  # Coefficients of the constraints
    b = [300, 100, 0, 200, -50]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    amount_of_honey = -res.fun  # Maximum amount of honey transported

    return int(amount_of_honey)