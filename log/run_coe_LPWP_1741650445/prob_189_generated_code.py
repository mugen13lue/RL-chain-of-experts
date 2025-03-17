import gurobipy as gp
from gurobipy import GRB

def prob_189(num_trips_high_pressure, num_trips_liquefied_tanker):
    """
    Args:
        num_trips_high_pressure: an integer representing the number of trips using the high-pressure tube method.
        num_trips_liquefied_tanker: an integer representing the number of trips using the liquefied hydrogen tanker method.
    
    Returns:
        obj: an integer representing the total number of trips.
    """
    
    # Create a new model
    model = gp.Model("transportation_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of trips using high-pressure tube trailers
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of trips using liquefied hydrogen tankers
    
    # Set objective function: Minimize total number of trips
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(50*x + 30*y >= 1000, "volume_constraint")
    model.addConstr(500*x + 200*y <= 3750, "cost_constraint")
    model.addConstr(x <= y, "trip_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the total number of trips
    obj = model.objVal
    
    return obj