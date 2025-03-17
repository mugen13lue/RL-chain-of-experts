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
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")
    
    # Set objective function
    model.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(50*x + 200*y >= 100000, "min_jam_volume")
    model.addConstr(y <= x, "large_small_jars")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj