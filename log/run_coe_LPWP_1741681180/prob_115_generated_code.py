import pulp

def prob_115(fertilizer, seeds):
    """
    Args:
        fertilizer: an integer, the number of units of fertilizer
        seeds: an integer, the number of units of seeds
    Returns:
        obj: an integer, the total time it takes for the lawn to be ready
    """
    obj = 0
    
    # Define the LP problem
    prob = pulp.LpProblem("Minimize Total Time", pulp.LpMinimize)
    
    # Define decision variables
    x = pulp.LpVariable("fertilizer_units", lowBound=50, upBound=None, cat='Continuous')
    y = pulp.LpVariable("seeds_units", lowBound=0, upBound=None, cat='Continuous')
    
    # Objective function
    prob += 0.5*x + 1.5*y
    
    # Constraints
    prob += x + y <= 300
    prob += x >= 50
    prob += x <= 2*y
    
    # Solve the LP problem
    prob.solve()
    
    # Get the optimal objective value
    obj = pulp.value(prob.objective)
    
    return obj