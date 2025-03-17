from scipy.optimize import linprog

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
    c = [-1, -1]  # Coefficients of the objective function to maximize x + y
    A = [[0, 0], [kids_size_bottle_capacity, adult_size_bottle_capacity], [-ratio, 1]]  # Coefficients of the inequality constraints
    b = [0, available_cough_syrup, 0]  # Right-hand side of the inequality constraints
    bounds = [(50, None), (0, None)]  # Bounds for the decision variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    number_of_bottles = res.fun * -1  # Maximum total number of bottles

    return int(number_of_bottles)