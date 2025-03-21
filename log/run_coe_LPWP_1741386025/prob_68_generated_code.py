def prob_68(kids_size_bottle_capacity, adult_size_bottle_capacity, ratio, available_cough_syrup):
    """
    Args:
        kids_size_bottle_capacity: an integer, the capacity of kids size bottle
        adult_size_bottle_capacity: an integer, the capacity of adult size bottle
        ratio: an integer, the ratio of adult size bottle to kids size bottle
        available_cough_syrup: an integer, the total amount of cough syrup available
    Returns:
        number_of_bottles: an integer, the maximum total number of bottles that can be produced
    """
    from scipy.optimize import linprog

    c = [-1, -1]  # Coefficients of the objective function to maximize x + y
    A = [[kids_size_bottle_capacity, adult_size_bottle_capacity], [-1, 0], [0, -1], [-ratio, 1]]  # Coefficients of the constraints
    b = [available_cough_syrup, 0, 0, 0]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(50, None))

    return int(res.x[0] + res.x[1])  # Total number of bottles