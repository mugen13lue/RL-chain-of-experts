from scipy.optimize import linprog

def prob_118(vitamin_shots, pills, vitamin_c_shot, vitamin_d_shot, vitamin_c_pill, vitamin_d_pill, max_shots, people_per_pill):
    """
    Args:
        vitamin_shots: an integer, the number of batches of vitamin shots
        pills: an integer, the number of batches of vitamin pills
        vitamin_c_shot: an integer, the number of units of vitamin C required for a batch of vitamin shots
        vitamin_d_shot: an integer, the number of units of vitamin D required for a batch of vitamin shots
        vitamin_c_pill: an integer, the number of units of vitamin C required for a batch of vitamin pills
        vitamin_d_pill: an integer, the number of units of vitamin D required for a batch of vitamin pills
        max_shots: an integer, the maximum number of batches of vitamin shots
        people_per_pill: an integer, the number of people supplied by one batch of vitamin pills
    Returns:
        obj: an integer, the maximum number of people that can be supplied
    """
    c = [-10, -7]  # Coefficients of the objective function to maximize 10x + 7y

    A = [[vitamin_c_shot, vitamin_c_pill], [vitamin_d_shot, vitamin_d_pill], [-1, 0], [0, -1], [1, -1]]  # Coefficients of the constraints
    b = [1200, 1500, 0, 0, 0]  # Right-hand side of the constraints

    bounds = [(0, max_shots), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return int(-res.fun)  # Return the maximum number of people that can be supplied