def prob_78(small, large, twice):
    """
    Args:
        small: an integer, representing the number of small crates
        large: an integer, representing the number of large crates
        twice: an integer, representing the requirement of large crates being twice the number of small crates

    Returns:
        obj: an integer, representing the objective value (number of crates produced)
    """
    
    # Import the PuLP library for linear programming
    from pulp import LpProblem, LpMaximize, LpVariable
    
    # Create the LP problem
    prob = LpProblem("Maximize Crates Produced", LpMaximize)
    
    # Define the decision variables
    x = LpVariable("small_crates", lowBound=5, cat='Integer')
    y = LpVariable("large_crates", lowBound=2*small, cat='Integer')
    
    # Add the objective function
    prob += x + y
    
    # Add the constraints
    prob += 20*x + 50*y <= 500
    prob += y >= 2*x
    
    # Solve the LP problem
    prob.solve()
    
    # Return the optimal number of crates produced
    return int(x.varValue), int(y.varValue)