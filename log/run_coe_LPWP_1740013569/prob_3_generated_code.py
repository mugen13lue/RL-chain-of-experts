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
    A = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # Coefficients of the inequality constraints
    b = [constraint2, constraint3, -apples, -pears]  # Right-hand side of the inequality constraints
    if constraint4:
        A.append([-2, 1])
        b.append(0)
    bounds = [(5, None), (10, None)]  # Bounds for the variables x (apples) and y (pears)

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = -res.fun  # Optimal profit is the negative of the minimum value found by linprog
    return obj