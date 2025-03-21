import pulp

def prob_162(bus, car):
    """
    Args:
        bus: an integer (number of bus trips)
        car: an integer (number of car trips)
    
    Returns:
        obj: an integer (total time required to transport the monkeys)
    """
    # Create a LP minimization problem
    prob = pulp.LpProblem("MonkeyTransport", pulp.LpMinimize)
    
    # Define decision variables
    x = pulp.LpVariable("bus_trips", lowBound=0, upBound=10, cat='Integer')
    y = pulp.LpVariable("car_trips", lowBound=0, cat='Integer')
    
    # Add constraints
    prob += 20*x + 6*y >= 300
    prob += y >= 0.6*(x + y)
    
    # Define objective function
    prob += 30*x + 15*y
    
    # Solve the problem
    prob.solve()
    
    # Return the total time required
    return int(pulp.value(prob.objective))