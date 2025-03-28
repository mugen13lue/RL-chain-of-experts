from gurobipy import *

def prob_98(vintage_bottles, regular_bottles):
    """
    Args:
        vintage_bottles: an integer (number of vintage bottles)
        regular_bottles: an integer (number of regular bottles)
    Returns:
        obj: an integer (maximum total number of bottles produced)
    """
    
    # Create a new model
    m = Model("Vine Bottles Production")
    
    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="vintage_bottles")
    y = m.addVar(vtype=GRB.INTEGER, name="regular_bottles")
    
    # Set objective
    m.setObjective(x + y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    m.addConstr(500*x + 750*y <= 100000, "total_vine_constraint")
    m.addConstr(y >= 4*x, "min_regular_bottles_constraint")
    m.addConstr(x >= 10, "min_vintage_bottles_constraint")
    
    # Optimize model
    m.optimize()
    
    # Get the optimal objective value
    obj = int(m.objVal)
    
    return obj