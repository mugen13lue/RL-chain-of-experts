import gurobipy as gp
from gurobipy import GRB

def prob_29(regular_mix, sour_surprise_mix, constraint1, constraint2):
    """
    Args:
        regular_mix: a float, the amount of regular mix candy created
        sour_surprise_mix: a float, the amount of sour surprise mix candy created
        constraint1: an integer, the limit of available regular candy
        constraint2: an integer, the limit of available sour candy
    Returns:
        obj: a float, the maximum profit achieved
    """
    
    # Create a new model
    model = gp.Model("candy_store")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="regular_mix")
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="sour_surprise_mix")
    
    # Set objective function
    model.setObjective(3*x + 5*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(0.8*x + 0.1*y <= constraint1, "regular_candy_constraint")
    model.addConstr(0.2*x + 0.9*y <= constraint2, "sour_candy_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the maximum profit achieved
    obj = model.objVal
    
    return obj