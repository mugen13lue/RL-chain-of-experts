from scipy.optimize import linprog

def prob_266(acai_berry_smoothie, banana_chocolate_smoothie):
    """
    Args:
        acai_berry_smoothie: an integer, represents the number of acai berry smoothies
        banana_chocolate_smoothie: an integer, represents the number of banana chocolate smoothies
    Returns:
        amount_of_water: an integer, total amount of water used
    """
    c = [3, 4]  # Coefficients of the objective function to minimize total amount of water used
    A = [[7, 3], [6, 4], [-1, -1], [-0.35, -0.65], [-1, 1]]  # Coefficients of the inequality constraints
    b = [3500, 3200, 0, 0, 0]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    amount_of_water = res.fun  # Total amount of water used

    return amount_of_water