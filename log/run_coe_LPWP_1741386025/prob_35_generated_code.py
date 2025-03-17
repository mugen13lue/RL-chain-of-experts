from scipy.optimize import linprog

def prob_35(pill_A, pill_B, sleep_inducing_constraint, anti_inflammatory_constraint):
    """
    Args:
        pill_A: an integer, number of pill A
        pill_B: an integer, number of pill B
        sleep_inducing_constraint: an integer, constraint value for sleep inducing medicine
        anti_inflammatory_constraint: an integer, constraint value for anti-inflammatory medicine
    Returns:
        cost: an integer, minimum cost
    """
    c = [4, 5]  # Cost per pill A and pill B
    A = [[-3, -6], [-5, -1]]  # Coefficients of sleep inducing and anti-inflammatory medicine in pill A and pill B
    b = [-sleep_inducing_constraint, -anti_inflammatory_constraint]  # Constraints for sleep inducing and anti-inflammatory medicine
    bounds = [(0, None), (0, None)]  # Non-negativity constraints for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return int(res.fun)