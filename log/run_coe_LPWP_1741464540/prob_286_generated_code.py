from scipy.optimize import linprog

def prob_286(wine, kombucha, fruit_wine, water_wine, fruit_kombucha, tea_kombucha, water_available, tea_available, kombucha_min_percent):
    """
    Args:
        wine: an integer representing the number of wine units
        kombucha: an integer representing the number of kombucha units
        fruit_wine: an integer representing the units of fruit required for wine
        water_wine: an integer representing the units of water required for wine
        fruit_kombucha: an integer representing the units of fruit required for kombucha
        tea_kombucha: an integer representing the units of tea required for kombucha
        water_available: an integer representing the available units of water
        tea_available: an integer representing the available units of tea
        kombucha_min_percent: an integer representing the minimum percentage of kombucha production

    Returns:
        obj: an integer representing the objective value
    """
    c = [fruit_wine, fruit_kombucha]  # Coefficients of the objective function to minimize (fruit_wine * wine + fruit_kombucha * kombucha)
    A = [[fruit_wine, fruit_kombucha], [water_wine, tea_kombucha], [-1, 1], [0, -kombucha_min_percent]]  # Coefficients of the constraints
    b = [water_available, tea_available, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun