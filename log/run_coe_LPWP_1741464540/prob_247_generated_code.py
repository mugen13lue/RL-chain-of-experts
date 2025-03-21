from scipy.optimize import linprog

def prob_247(small_packets, jugs, _1000, _1250, three_times, _35, _65000):
    """
    Solves the optimization problem of maximizing the total number of units that can be sold to customers.

    Args:
        small_packets: an integer, number of sets of small packets
        jugs: an integer, number of jugs
        _1000: an integer, capacity of small packets in ml
        _1250: an integer, capacity of jugs in ml
        three_times: a string, indicating the relationship between jugs and small packets
        _35: an integer, minimum number of small packets to be filled
        _65000: an integer, total amount of jam available in ml

    Returns:
        total_number_of_units: an integer, maximum total number of units that can be sold
    """
    c = [-1, -1]  # Coefficients for the objective function to maximize Z = x + y
    A = [[-1000, -1250], [0, -3], [1, 0]]  # Coefficients for the constraints
    b = [-_65000, 0, _35]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    total_number_of_units = -res.fun  # Maximum total number of units that can be sold

    return total_number_of_units