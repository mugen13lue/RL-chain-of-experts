from scipy.optimize import linprog

def prob_30(phones, laptops, var1, var2, var3, var4, var5, var6):
    """
    Args:
        phones: an integer, representing the number of phones
        laptops: an integer, representing the number of laptops
        var1: an integer, representing the labor hours required for phones
        var2: an integer, representing the labor hours required for laptops
        var3: an integer, representing the cost per sq. foot for phone production
        var4: an integer, representing the cost per sq. foot for laptop production
        var5: an integer, representing the net revenue per sq. foot for phones
        var6: an integer, representing the net revenue per sq. foot for laptops

    Returns:
        obj: an integer, the optimal revenue
    """
    c = [-var5, -var6]  # Coefficients for maximizing revenue
    A = [[1, 1], [var1, var2], [var3, var4]]  # Coefficients for constraints
    b = [100, 2000, 5000]  # RHS of constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return -res.fun  # Return the optimal revenue