import gurobipy as gp
from gurobipy import GRB

def prob_189(var1, var2):
    """
    Args:
        var1: an integer representing the number of trips using the high-pressure tube method.
        var2: an integer representing the number of trips using the liquefied hydrogen tanker method.
    
    Returns:
        obj: an integer representing the total number of trips.
    """
    
    # Create a new model
    model = gp.Model("transportation_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of trips using high-pressure tube trailers
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of trips using liquefied hydrogen tankers
    
    # Set objective: minimize total number of trips
    model.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(500*x + 200*y <= 3750, "budget_constraint")  # Total cost constraint
    model.addConstr(50*x + 30*y >= 1000, "transport_constraint")  # Total amount of hydrogen constraint
    model.addConstr(x < y, "trip_constraint")  # Number of trips constraint
    
    # Optimize model
    model.optimize()
    
    # Get the total number of trips
    obj = model.objVal
    
    return obj