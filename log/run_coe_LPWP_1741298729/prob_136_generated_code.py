from scipy.optimize import linprog

def prob_136(hours_lab_1, hours_lab_2, available_worker_hours, min_heart_pills, min_lung_pills):
    """
    Args:
        hours_lab_1: an integer representing the number of hours to run lab 1
        hours_lab_2: an integer representing the number of hours to run lab 2
        available_worker_hours: an integer representing the available worker hours
        min_heart_pills: an integer representing the minimum number of heart medication pills
        min_lung_pills: an integer representing the minimum number of lung medication pills
    Returns:
        obj: an integer representing the total time needed
    """
    c = [3, 5]  # Coefficients of the objective function to minimize total time needed
    A = [[-3, -5], [20, 30], [30, 40]]  # Coefficients of the inequality constraints
    b = [-available_worker_hours, min_heart_pills, min_lung_pills]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables hours_lab_1 and hours_lab_2

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun