from scipy.optimize import linprog

def maximize_profit(blueberries, raspberries, total_acres, watering_cost_limit, labor_days_limit):
    """
    Args:
        blueberries: an integer, representing the number of acres for blueberries.
        raspberries: an integer, representing the number of acres for raspberries.
        total_acres: an integer, representing the total available acres.
        watering_cost_limit: an integer, representing the limit for watering cost.
        labor_days_limit: an integer, representing the limit for labor days.

    Returns:
        obj: an integer, representing the objective value (profit).
    """
    
    # Coefficients of the objective function
    c = [-56, -75]  # maximize profit
    
    # Coefficients of the inequality constraints
    A = [[6, 3], [22, 25], [1, 1]]  # labor days, watering costs, total acres
    b = [labor_days_limit, watering_cost_limit, total_acres]
    
    # Bounds for the variables
    x_bounds = (0, None)  # non-negative values for blueberries and raspberries
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds])
    
    return -res.fun  # return the negative of the objective value to maximize profit