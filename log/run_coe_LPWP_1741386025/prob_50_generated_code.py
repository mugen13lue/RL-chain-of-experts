from scipy.optimize import linprog

def prob_50(staff_teachers, substitute_teachers, requires_constraint, budget_constraint):
    """
    Args:
        staff_teachers: an integer, indicating the number of staff teachers
        substitute_teachers: an integer, indicating the number of substitute teachers
        requires_constraint: an integer, indicating the number of teaching availability required
        budget_constraint: an integer, indicating the budget limit
    Returns:
        total_number_of_teachers: an integer, indicating the total number of teachers
    """
    c = [1, 1]  # Coefficients of the objective function to minimize (x + y)
    A = [[6, 3], [-300, -100]]  # Coefficients of the inequality constraints
    b = [requires_constraint, -budget_constraint]  # Right-hand side of the inequality constraints
    bounds = [(0, None), (0, None)]  # Bounds for the variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    total_number_of_teachers = res.x[0] + res.x[1]
    return int(total_number_of_teachers)