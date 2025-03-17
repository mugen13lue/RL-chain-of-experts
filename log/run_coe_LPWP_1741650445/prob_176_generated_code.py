import gurobipy as gp
from gurobipy import GRB

def prob_176(small, large):
    """
    Args:
        small: an integer, number of small jars
        large: an integer, number of large jars
    Returns:
        obj: an integer, the objective value
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("jam_shipping")
    
    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="small_jars")
    y = model.addVar(vtype=GRB.INTEGER, name="large_jars")
    
    # Set objective: minimize the total number of jars used
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(50*x + 200*y >= 100000, "min_jam_requirement")
    model.addConstr(y <= x, "large_small_jars_limit")
    
    # Optimize model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj