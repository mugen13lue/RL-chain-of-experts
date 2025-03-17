from gurobipy import *

def prob_186(cows, elephants):
    """
    Args:
        cows: an integer, number of cows
        elephants: an integer, number of elephants
    Returns:
        obj: an integer, objective value
    """
    
    # Create a new model
    m = Model("BrickTransport")
    
    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="cows")
    y = m.addVar(vtype=GRB.INTEGER, name="elephants")
    
    # Set objective: Minimize z = x + y
    m.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    m.addConstr(x >= 0, "cows_nonneg")
    m.addConstr(y >= 0, "elephants_nonneg")
    m.addConstr(20*x + 50*y >= 1000, "bricks_requirement")
    m.addConstr(y <= x, "elephants_limit")
    m.addConstr(x <= 2*y, "cows_limit")
    
    # Optimize the model
    m.optimize()
    
    # Get the objective value
    obj = m.objVal
    
    return obj