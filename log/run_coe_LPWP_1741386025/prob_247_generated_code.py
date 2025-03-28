from scipy.optimize import linprog

def prob_247(small_packets, jugs, _1000, _1250, three_times, _35, _65000):
    """
    Args:
        small_packets: an integer, number of sets of small packets
        jugs: an integer, number of jugs
        _1000: an integer, capacity of small packets
        _1250: an integer, capacity of jugs
        three_times: an integer, multiplier for jugs compared to small packets
        _35: an integer, minimum number of small packets
        _65000: an integer, total amount of jam available
    Returns:
        total_number_of_units: an integer, maximum total number of units that can be sold
    """
    c = [-1, -1]  # Coefficients of the objective function to maximize x + y
    A = [[_1000, _1250], [-1, 0], [0, -1]]  # Coefficients of the inequality constraints
    b = [_65000, -_35, -three_times*_35]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    total_number_of_units = int(-res.fun)  # Maximum total number of units that can be sold
    return total_number_of_units