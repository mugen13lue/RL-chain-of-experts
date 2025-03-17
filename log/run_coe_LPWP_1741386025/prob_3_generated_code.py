from scipy.optimize import linprog

def prob_3(apples, pears, constraint1, constraint2, constraint3, constraint4):
    """
    Args:
        apples: an integer - number of acres of apples to grow
        pears: an integer - number of acres of pears to grow
        constraint1: an integer - total available land in acres
        constraint2: an integer - minimum required acres of apples
        constraint3: an integer - minimum required acres of pears
        constraint4: a boolean - whether the pears should be at most twice the apples or not
    Returns:
        obj: an integer - optimal profit
    """
    c = [-2, -4]  # Coefficients of the objective function to maximize profit
    A = [[1, 1], [0, 1], [-2, 1]]  # Coefficients of the constraints
    b = [constraint1, constraint3, 0]  # Right-hand side of the constraints
    bounds = [(constraint2, None), (constraint3, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = -res.fun  # Optimal profit

    return obj