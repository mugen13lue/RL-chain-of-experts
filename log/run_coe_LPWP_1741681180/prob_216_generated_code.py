from scipy.optimize import linprog

def prob_216(crepe_cakes, sponge_cakes, birthday_cakes):
    """
    Maximizes the profit of a small bakery by determining the number of each cake to make.

    Args:
        crepe_cakes: Integer, the number of crepe cakes to make.
        sponge_cakes: Integer, the number of sponge cakes to make.
        birthday_cakes: Integer, the number of birthday cakes to make.
        
    Returns:
        profit: Float, the maximum profit achievable.
    """
    c = [-12, -10, -15]  # Coefficients of the objective function to minimize (-12x1 - 10x2 - 15x3)
    A = [[400, 500, 450], [200, 300, 350]]  # Coefficients of the inequality constraints
    b = [20000, 14000]  # Right-hand side of the inequality constraints
    x_bounds = (0, None)  # Bounds for the variables x1, x2, x3

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds, x_bounds], method='highs')

    return -res.fun  # Return the maximum profit