def prob_107(fish, chicken):
    """
    Args:
        fish: an integer, number of fish meals
        chicken: an integer, number of chicken meals
    Returns:
        obj: an integer, minimized fat intake
    """
    from scipy.optimize import linprog

    c = [7, 10]  # Coefficients of fat in fish and chicken meals
    A = [[10, 15], [12, 8], [-2, 1]]  # Coefficients of protein and iron in fish and chicken meals, and preference constraint
    b = [130, 120, 0]  # Minimum required protein and iron intake, and preference constraint value

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return int(res.fun)