import gurobipy as gp
from gurobipy import GRB

def prob_166(large, small, large_planes, small_planes):
    """
    Args:
        large: an integer, the number of large planes
        small: an integer, the number of small planes
        large_planes: an integer, the number of large planes
        small_planes: an integer, the number of small planes
    Returns:
        obj: an integer, the objective value
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("plane_optimization")
    
    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="large_planes")
    y = model.addVar(vtype=GRB.INTEGER, name="small_planes")
    
    # Set objective function
    model.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 10*y >= 300, "min_cars")
    model.addConstr(x <= large, "max_large_planes")
    model.addConstr(y <= small, "max_small_planes")
    model.addConstr(x < y, "large_less_than_small")
    
    # Optimize model
    model.optimize()
    
    # Get objective value
    obj = model.objVal
    
    return obj