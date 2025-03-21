from scipy.optimize import linprog

def prob_184(medium, large, _2, _30, _4, _70, three, _60, _5):
    """
    Args:
        medium: an integer, the number of medium sized carts
        large: an integer, the number of large sized carts
        _2: an integer, horse requirement for medium sized cart
        _30: an integer, rice carrying capacity of medium sized cart
        _4: an integer, horse requirement for large sized cart
        _70: an integer, rice carrying capacity of large sized cart
        three: an integer, ratio of medium to large sized carts
        _60: an integer, available horses
        _5: an integer, minimum number of medium and large sized carts
    Returns:
        amount_of_rice: an integer, maximum amount of rice that can be transported
    """
    c = [-30, -70]  # Coefficients of the objective function to maximize -30x - 70y

    A = [[2, 4], [-1, 0], [0, -1], [-3, 1]]  # Coefficients of the constraints
    b = [60, -5, -5, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(5, None), (5, None)])  # Using linear programming to maximize the objective function

    amount_of_rice = -res.fun  # Maximum amount of rice that can be transported

    return int(amount_of_rice)