from gurobipy import *

def prob_225(wide_pipes, narrow_pipes):
    """
    Args:
        wide_pipes: an integer representing the number of wide pipes
        narrow_pipes: an integer representing the number of narrow pipes
    Returns:
        obj: an integer representing the minimum total number of pipes required
    """
    obj = 1e9
    
    # Create a new model
    m = Model("pipe_optimization")
    
    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="wide_pipes")
    y = m.addVar(vtype=GRB.INTEGER, name="narrow_pipes")
    
    # Set objective
    m.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    m.addConstr(25*x + 15*y >= 900, "water_requirement")
    m.addConstr(x >= 5, "min_wide_pipes")
    m.addConstr(x <= y/3, "max_wide_pipes")
    
    # Optimize model
    m.optimize()
    
    # Get the minimum total number of pipes required
    obj = m.objVal
    
    return obj