import gurobipy as gp
from gurobipy import GRB

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
    model = gp.Model("pipe_transportation")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="wide_pipes")
    y = model.addVar(vtype=GRB.INTEGER, name="narrow_pipes")
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(25*x + 15*y >= 900, "water_transported")
    model.addConstr(x >= 5, "minimum_wide_pipes")
    model.addConstr(x <= (1/3)*y, "wide_pipes_limit")
    
    # Optimize model
    model.optimize()
    
    # Get the minimum total number of pipes required
    obj = model.objVal
    
    return obj