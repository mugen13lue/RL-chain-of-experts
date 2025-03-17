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
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of large planes
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of small planes
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 10*y >= 300, "total_cars")
    model.addConstr(x <= y, "large_small_planes")
    model.addConstr(x >= 0, "non_negativity_x")
    model.addConstr(y >= 0, "non_negativity_y")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj