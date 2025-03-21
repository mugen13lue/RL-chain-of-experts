from scipy.optimize import linprog

def prob_45(blueberries, raspberries, constraint1, constraint2, constraint3):
    """
    Args:
        blueberries: an integer, representing the number of acres for blueberries.
        raspberries: an integer, representing the number of acres for raspberries.
        constraint1: an integer, representing the limit for total acres.
        constraint2: an integer, representing the limit for watering cost.
        constraint3: an integer, representing the limit for labor days.

    Returns:
        obj: an integer, representing the objective value (profit).
    """
    c = [-56, -75]  # Coefficients of the objective function to minimize (-56x - 75y)
    A = [[6, 3], [22, 25]]  # Coefficients of the inequality constraints
    b = [constraint3, constraint2]  # Right-hand side of the inequality constraints
    bounds = [(0, constraint1), (0, constraint1)]  # Bounds for x and y (0 to total acres)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = -res.fun  # Maximum profit is the negative of the minimum value obtained by linprog

    return obj