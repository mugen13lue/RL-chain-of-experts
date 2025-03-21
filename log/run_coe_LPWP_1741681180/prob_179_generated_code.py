import pulp

def prob_179(cargo_planes, ultrawide_trucks):
    """
    Args:
        cargo_planes: an integer, number of cargo planes
        ultrawide_trucks: an integer, number of ultrawide trucks
    Returns:
        obj: an integer, minimum number of trips
    """
    
    # Create a LP minimization problem
    prob = pulp.LpProblem("Minimize Trips", pulp.LpMinimize)
    
    # Define decision variables
    x = pulp.LpVariable("x", lowBound=0, cat='Integer')  # Number of trips made by cargo planes
    y = pulp.LpVariable("y", lowBound=0, cat='Integer')  # Number of trips made by ultrawide trucks
    
    # Objective function to minimize total trips
    prob += x + y
    
    # Constraints
    prob += 10*x + 6*y >= 200  # Total number of tires transported constraint
    prob += 1000*x + 700*y <= 22000  # Total cost constraint
    prob += x <= y  # Plane trips cannot exceed truck trips
    
    # Solve the LP problem
    prob.solve()
    
    # Return the minimum number of trips
    return int(pulp.value(prob.objective))