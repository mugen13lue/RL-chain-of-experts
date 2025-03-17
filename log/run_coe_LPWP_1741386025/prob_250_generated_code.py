from scipy.optimize import linprog

def prob_250(cans, glass_bottles, required_capacity, constraint2, constraint3):
    """
    Args:
        cans: an integer, representing the number of cans produced
        glass_bottles: an integer, representing the number of glass bottles produced
        required_capacity: an integer, representing the minimum required capacity in ml
        constraint2: an integer, representing the multiplier for cans compared to glass bottles
        constraint3: an integer, representing the minimum number of glass bottles required
    Returns:
        cans: an integer, representing the optimal number of cans to produce
        glass_bottles: an integer, representing the optimal number of glass bottles to produce
    """
    c = [-1, -1]  # Coefficients for the objective function to maximize x + y
    A = [[250, 1000], [0, -1], [-constraint2, 1]]  # Coefficients for the constraints
    b = [required_capacity, -constraint3, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    return int(res.x[0]), int(res.x[1])