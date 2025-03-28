from scipy.optimize import linprog

def prob_59(num_lychee_bubble_teas, num_mango_bubble_teas, mango_juice_limit, lychee_juice_limit, lychee_flavored_limit):
    """
    Args:
        num_lychee_bubble_teas: an integer representing the number of lychee bubble teas made
        num_mango_bubble_teas: an integer representing the number of mango bubble teas made
        mango_juice_limit: an integer representing the limit of mango juice available
        lychee_juice_limit: an integer representing the limit of lychee juice available
        lychee_flavored_limit: an integer representing the minimum number of lychee flavored bubble teas required
    Returns:
        amount_of_tea: an integer representing the total amount of tea needed
    """
    c = [8, 6]  # Coefficients of the objective function (tea amounts)
    A = [[4, 0], [0, 6], [8, 6], [-0.4, -0.4], [-1, 1]]  # Coefficients of the constraints
    b = [mango_juice_limit, lychee_juice_limit, float('inf'), lychee_flavored_limit, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    if res.success:
        return res.fun  # Total amount of tea needed
    else:
        return "Optimization failed"