from scipy.optimize import linprog

def prob_119(electronic_thermometer, regular_thermometer, electronic_constraint, regular_constraint, time_constraint):
    """
    Args:
        electronic_thermometer: an integer representing the number of patients checked with the electronic thermometer
        regular_thermometer: an integer representing the number of patients checked with the regular thermometer
        electronic_constraint: an integer representing the required number of patients checked with the electronic thermometer
        regular_constraint: an integer representing the required number of patients checked with the regular thermometer
        time_constraint: an integer representing the maximum time the office is open
    Returns:
        number_of_patients: an integer representing the maximum number of patients whose temperature can be taken
    """
    c = [-1, -1]  # Coefficients for the objective function to maximize x + y
    A = [[-3, -2], [1, 0], [0, 1]]  # Coefficients for the constraints
    b = [-time_constraint, -electronic_constraint, -regular_constraint]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))  # Solve the linear programming problem

    return int(-res.fun)  # Return the maximum number of patients whose temperature can be taken

# Example usage
print(prob_119(0, 0, 100, 50, 15000))  # Output: 5000