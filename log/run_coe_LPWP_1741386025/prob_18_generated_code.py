from scipy.optimize import linprog

def prob_18(Feed_A, Feed_B):
    """
    Args:
        Feed_A: an integer, representing the amount of Feed A
        Feed_B: an integer, representing the amount of Feed B
    Returns:
        obj: an integer, representing the minimum cost of the mixture
    """
    c = [100, 80]  # Cost coefficients for Feed A and Feed B
    A = [[-10, -7], [-8, -15]]  # Coefficients for protein and fat constraints
    b = [-30, -50]  # Right-hand side of constraints
    bounds = [(0, None), (0, None)]  # Non-negativity bounds for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = res.fun

    return obj