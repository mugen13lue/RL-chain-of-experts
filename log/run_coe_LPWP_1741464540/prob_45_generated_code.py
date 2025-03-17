from scipy.optimize import linprog

def maximize_profit(blueberries, raspberries, total_acres, watering_cost_limit, labor_days_limit):
    """
    Args:
        blueberries: an integer, representing the number of acres for blueberries.
        raspberries: an integer, representing the number of acres for raspberries.
        total_acres: an integer, representing the total available acres for planting.
        watering_cost_limit: an integer, representing the limit for watering cost.
        labor_days_limit: an integer, representing the limit for labor days.

    Returns:
        obj: an integer, representing the maximum profit value.
    """
    c = [-56, -75]  # Coefficients of the objective function to be maximized (56x + 75y)
    A = [[6, 3], [22, 25]]  # Coefficients of the inequality constraints
    b = [labor_days_limit, watering_cost_limit]  # Right-hand side of the inequality constraints
    bounds = [(0, total_acres), (0, total_acres)]  # Bounds for x and y (0 to total acres)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = res.fun  # Maximum profit value obtained by linprog

    return obj