import gurobipy as gp
from gurobipy import GRB

def prob_147(num_beam_bridges, num_truss_bridges):
    """
    Args:
        num_beam_bridges: an integer, representing the number of beam bridges
        num_truss_bridges: an integer, representing the number of truss bridges
        
    Returns:
        obj: an integer, representing the maximum total mass that can be supported
    """
    
    # Create a new model
    model = gp.Model("bridge_building")
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="beam_bridges")
    y = model.addVar(vtype=GRB.INTEGER, name="truss_bridges")
    
    # Set objective function
    model.setObjective(40*x + 60*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 50*y <= 600, "popsicle_sticks")
    model.addConstr(5*x + 8*y <= 100, "glue")
    model.addConstr(y <= 5, "truss_bridges_limit")
    model.addConstr(x >= y, "beam_bridges_more_than_truss")
    
    # Optimize the model
    model.optimize()
    
    # Get the maximum total mass
    obj = model.objVal
    
    return obj