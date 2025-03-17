import gurobipy as gp
from gurobipy import GRB

def prob_98(vintage_bottles, regular_bottles):
    """
    Args:
        vintage_bottles: an integer (number of vintage bottles)
        regular_bottles: an integer (number of regular bottles)
    Returns:
        obj: an integer (maximum total number of bottles produced)
    """
    
    # Create a new model
    model = gp.Model("vine_production")
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="vintage_bottles")
    y = model.addVar(vtype=GRB.INTEGER, name="regular_bottles")
    
    # Objective function: maximize total number of bottles produced
    model.setObjective(x + y, sense=GRB.MAXIMIZE)
    
    # Constraints
    model.addConstr(500*x + 750*y <= 100000, "total_vine_constraint")
    model.addConstr(y >= 4*x, "min_regular_bottles_constraint")
    model.addConstr(x >= 10, "min_vintage_bottles_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = int(model.objVal)
    
    return obj