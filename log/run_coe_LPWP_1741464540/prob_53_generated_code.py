from scipy.optimize import linprog

def prob_53(process_A, process_B):
    """
    Args:
        process_A: an integer, number of processes of type A
        process_B: an integer, number of processes of type B
    Returns:
        obj: an integer, maximum number of coins that can be plated
    """
    c = [-5, -7]  # Coefficients of the objective function to maximize 5x + 7y
    A = [[3, 5], [2, 3]]  # Coefficients of the constraints
    b = [500, 300]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(-res.fun)  # Return the maximum number of coins that can be plated