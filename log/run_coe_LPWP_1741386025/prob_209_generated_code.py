from scipy.optimize import linprog

def prob_209(regular_brand, premium_brand):
    """
    Args:
        regular_brand: an integer representing the number of bags of regular brand
        premium_brand: an integer representing the number of bags of premium brand
    Returns:
        obj: an integer representing the minimum cost
    """
    c = [20, 35]  # Cost coefficients for regular and premium brands
    A = [[-4, -12], [-7, -10], [-10, -16]]  # Coefficients for calcium, vitamin mix, and protein constraints
    b = [-15, -20, -20]  # Minimum requirements for calcium, vitamin mix, and protein
    bounds = [(0, None), (0, None)]  # Non-negativity bounds for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    min_cost = res.fun
    return int(min_cost)