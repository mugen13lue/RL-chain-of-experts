from scipy.optimize import linprog

def prob_59(lychee_bubble_tea, mango_bubble_tea, mango_juice_limit, lychee_juice_limit, lychee_flavored_limit):
    """
    Args:
        lychee_bubble_tea: an integer representing the number of lychee bubble teas made
        mango_bubble_tea: an integer representing the number of mango bubble teas made
        mango_juice_limit: an integer representing the limit of mango juice available
        lychee_juice_limit: an integer representing the limit of lychee juice available
        lychee_flavored_limit: an integer representing the minimum number of lychee flavored bubble teas required
    Returns:
        amount_of_tea: an integer representing the total amount of tea needed
    """
    c = [8, 6]  # Coefficients of the objective function to minimize 8x + 6y
    A = [[4, 0], [0, 6], [8, 6], [-0.4, -0.4], [-1, 1]]  # Coefficients of the constraints
    b = [mango_juice_limit, lychee_juice_limit, mango_bubble_tea + lychee_bubble_tea, -lychee_flavored_limit, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    amount_of_tea = res.fun  # Total amount of tea needed

    return amount_of_tea