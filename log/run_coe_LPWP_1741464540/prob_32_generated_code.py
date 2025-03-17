from scipy.optimize import linprog

def prob_32(regular_model, premium_model, upperbound_regular_models, upperbound_premium_models, maximum_cars):
    """
    Args:
        regular_model: an integer, representing the number of regular models to make per day
        premium_model: an integer, representing the number of premium models to make per day
        upperbound_regular_models: an integer, representing the upper bound limit for regular models
        upperbound_premium_models: an integer, representing the upper bound limit for premium models
        maximum_cars: an integer, representing the maximum number of cars to make per day
    Returns:
        profit: an integer, representing the maximum profit achievable
    """
    c = [-5000, -8500]  # Coefficients of the objective function to minimize (-5000x1 - 8500x2)
    A = [[1, 0], [0, 1], [1, 1]]  # Coefficients of the inequality constraints
    b = [upperbound_regular_models, upperbound_premium_models, maximum_cars]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    profit = -res.fun  # Maximum profit achieved
    return profit