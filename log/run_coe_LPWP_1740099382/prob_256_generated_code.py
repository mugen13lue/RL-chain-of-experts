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
    obj = 0
    
    # Create a new model
    model = gp.Model("transportation_problem")
    
    # Define decision variables
    num_trains = model.addVar(lb=0, vtype=GRB.INTEGER, name="num_trains")
    num_trams = model.addVar(lb=0, vtype=GRB.INTEGER, name="num_trams")
    
    # Set objective function
    model.setObjective(num_trains + num_trams, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(num_trams >= 2*num_trains)
    model.addConstr(120*num_trains + 30*num_trams >= 600)
    
    # Optimize the model
    model.optimize()
    
    # Get the total number of transportation units required
    if model.status == GRB.OPTIMAL:
        obj = int(num_trains.x + num_trams.x)
    
    return obj