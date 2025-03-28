import pulp

def prob_54(miter_saw, circular_saw, constraint1, constraint2):
    """
    Args:
        miter_saw: an integer, the number of miter saws to purchase
        circular_saw: an integer, the number of circular saws to purchase
        constraint1: an integer, the result of the first constraint
        constraint2: an integer, the result of the second constraint
    Returns:
        number_of_saws: an integer, the total number of saws needed
    """
    
    # Create a LP minimization problem
    prob = pulp.LpProblem("Minimize Total Saws", pulp.LpMinimize)
    
    # Define decision variables
    x = pulp.LpVariable("x", lowBound=0, cat='Integer')  # Number of miter saws
    y = pulp.LpVariable("y", lowBound=0, cat='Integer')  # Number of circular saws
    
    # Objective function
    prob += x + y
    
    # Constraints
    prob += 50*x + 70*y >= constraint1
    prob += 60*x + 100*y <= constraint2
    
    # Solve the problem
    prob.solve()
    
    # Get the optimal values of x and y
    optimal_miter_saws = int(x.varValue)
    optimal_circular_saws = int(y.varValue)
    
    # Calculate the total number of saws needed
    number_of_saws = optimal_miter_saws + optimal_circular_saws
    
    return number_of_saws