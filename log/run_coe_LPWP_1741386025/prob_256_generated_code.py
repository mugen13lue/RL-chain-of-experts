import gurobipy as gp
from gurobipy import GRB

def prob_256(trains, trams) -> int:
    """
    Args:
        trains: Number of trains (an integer).
        trams: Number of trams (an integer).

    Returns:
        obj: Total number of transportation units (an integer).
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("transportation_problem")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="trains")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="trams")
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(y >= 2*x)
    model.addConstr(120*x + 30*y >= 600)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return int(obj)