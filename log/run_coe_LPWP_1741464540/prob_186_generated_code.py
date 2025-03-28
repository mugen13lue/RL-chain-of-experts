from gurobipy import *

def prob_186(cows, elephants):
    """
    Args:
        cows: an integer, number of cows
        elephants: an integer, number of elephants
    Returns:
        obj: an integer, objective value
    """
    obj = 1e9
    
    # Create a new model
    m = Model("animal_transportation")
    
    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="cows")
    y = m.addVar(vtype=GRB.INTEGER, name="elephants")
    
    # Set objective: minimize total number of animals
    m.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    m.addConstr(20*x + 50*y >= 1000, "min_bricks")
    m.addConstr(y <= x, "elephants_cows")
    m.addConstr(x <= 2*y, "cows_elephants")
    
    # Optimize model
    m.optimize()
    
    # Get objective value
    if m.status == GRB.OPTIMAL:
        obj = m.objVal
    
    return int(obj)