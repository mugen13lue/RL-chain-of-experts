from scipy.optimize import linprog

def prob_287(num_type_II_ambulance, num_hospital_van, constraint1, constraint2):
    """
    Solves the problem of minimizing the total cost to the hospital.

    Args:
        num_type_II_ambulance: Number of type II ambulances to schedule.
        num_hospital_van: Number of hospital vans to schedule.
        constraint1: The constraint that at least 320 patients need to be transported.
        constraint2: The constraint that at most 60% of shifts can be hospital vans.
    
    Returns:
        obj: The objective value representing the total cost.
    """
    
    # Coefficients of the objective function
    c = [820, 550]
    
    # Coefficients of the inequality constraints
    A = [[20, 15], [1, 1]]
    b = [320, num_type_II_ambulance + num_hospital_van]
    
    # Coefficients of the equality constraint
    A_eq = [[0, 1]]
    b_eq = [0.6 * (num_type_II_ambulance + num_hospital_van)]
    
    # Bounds for the variables
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=[x_bounds, y_bounds], method='highs')
    
    return res.fun