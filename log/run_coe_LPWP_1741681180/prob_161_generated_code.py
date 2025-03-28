from scipy.optimize import linprog

def prob_161(new_one, old_one, new_one_, old_one_):
    """
    Args:
        new_one: an integer, number of gifts delivered per trip by the new company
        old_one: an integer, number of gifts delivered per trip by the old company
        new_one_: an integer, liters of diesel used per trip by the new company
        old_one_: an integer, liters of diesel used per trip by the old company

    Returns:
        total_amount_of_diesel: an integer, total amount of diesel used
    """
    c = [new_one_, old_one_]  # Coefficients of the objective function to minimize
    A = [[-new_one, -old_one], [1, 1], [1, 0], [0, -1]]  # Coefficients of the inequality constraints
    b = [-1000, 0, 15, 0.4]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    total_amount_of_diesel = res.fun

    return total_amount_of_diesel