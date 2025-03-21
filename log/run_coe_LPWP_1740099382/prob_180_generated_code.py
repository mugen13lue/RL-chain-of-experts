import gurobipy as gp
from gurobipy import GRB

def prob_180(small, large):
    """
    Args:
        small: an integer, representing the number of small kegs
        large: an integer, representing the number of large kegs
    Returns:
        obj: an integer, representing the maximum amount of glacial water that can be transported
    """
    
    # Create a new model
    model = gp.Model("water_transportation")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of small kegs
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of large kegs
    
    # Set objective function
    model.setObjective(40*x + 100*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(x + y <= 25, "total_kegs")
    model.addConstr(y >= 5, "at_least_5_large_kegs")
    model.addConstr(x <= 30, "at_most_30_small_kegs")
    model.addConstr(y <= 10, "at_most_10_large_kegs")
    model.addConstr(x >= 2*y, "twice_as_many_small_kegs_as_large_kegs")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = int(model.objVal)
    
    return obj