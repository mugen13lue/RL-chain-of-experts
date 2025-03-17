from scipy.optimize import linprog

def prob_262(kayak, motorboat, constraint1):
    """
    Args:
        kayak: an integer representing the number of kayaks to be used
        motorboat: an integer representing the number of motorboats to be used
        constraint1: an integer representing the minimum number of locals to be moved
    Returns:
        obj: an integer representing the amount of time needed to transport all the locals
    """
    
    c = [5, 3]  # Coefficients of the objective function to minimize total time: 5x + 3y
    A = [[4, 5], [-1, 0], [0, -1]]  # Coefficients of the inequality constraints
    b = [constraint1, 0, -25]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    
    return res.fun