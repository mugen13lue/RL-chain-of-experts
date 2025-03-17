import gurobipy as gp
from gurobipy import GRB

def prob_17(chair, dresser, constraint1, constraint2):
    """
    Args:
        chair: an integer, the number of chairs produced by Elm Furniture
        dresser: an integer, the number of dressers produced by Elm Furniture
        constraint1: a float, the constraint for stain availability
        constraint2: a float, the constraint for oak wood availability
    Returns:
        obj: a float, the maximum profit
    """
    
    # Create a new model
    model = gp.Model("profit_maximization")
    
    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="chairs")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="dressers")
    
    # Set objective function
    model.setObjective(43*x + 52*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(1.4*x + 1.1*y <= constraint1, name="stain_constraint")
    model.addConstr(2*x + 3*y <= constraint2, name="oak_wood_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the maximum profit
    obj = model.objVal
    
    return obj