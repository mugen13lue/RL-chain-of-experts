def prob_109(automatic_machine, manual_machine):
    """
    Args:
        automatic_machine: an integer, representing the number of patients using the automatic machine
        manual_machine: an integer, representing the number of patients using the manual machine

    Returns:
        obj: an integer, representing the maximum number of patients whose blood pressure can be taken
    """
    
    # Import the PuLP optimization library
    from pulp import LpProblem, LpMaximize, LpVariable
    
    # Create the LP minimization problem
    prob = LpProblem("Maximize Patients", LpMaximize)
    
    # Define the variables
    x = LpVariable("x", lowBound=0, cat='Integer')  # Number of patients processed by automatic machine
    y = LpVariable("y", lowBound=0, cat='Integer')  # Number of patients processed by manual machine
    
    # Add the objective function
    prob += x + y
    
    # Add the constraints
    prob += 10*x + 15*y <= 20000
    prob += y >= 2*x
    prob += x <= 20
    
    # Solve the problem
    prob.solve()
    
    # Return the maximum number of patients
    return int(x.varValue + y.varValue)