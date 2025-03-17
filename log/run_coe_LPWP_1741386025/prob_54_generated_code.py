from scipy.optimize import linprog

def prob_54(miter_saw, circular_saw, constraint1, constraint2):
    """
    Args:
        miter_saw: an integer, the number of miter saws to purchase
        circular_saw: an integer, the number of circular saws to purchase
        constraint1: an integer, the result of the first constraint
        constraint2: an integer, the result of the second constraint
    Returns:
        result: a list of floats, the optimal number of miter saws and circular saws to purchase
    """
    c = [1, 1]  # Coefficients for the objective function to minimize x + y
    A = [[-50, -70], [60, 100]]  # Coefficients for the constraints
    b = [-constraint1, constraint2]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    return res.x

# Solve the woodshop problem
result = prob_54(1, 1, 1500, 2000)
print("Number of miter saws to purchase:", round(result[0]))
print("Number of circular saws to purchase:", round(result[1]))