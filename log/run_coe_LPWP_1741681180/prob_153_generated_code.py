import gurobipy as gp
from gurobipy import GRB

def prob_153(old_vans, new_vans):
    """
    Args:
        old_vans: an integer, the number of old vans
        new_vans: an integer, the number of new vans
    Returns:
        obj: an integer, the total amount of pollution produced
    """
    obj = 0
    
    # Create a new model
    model = gp.Model("minimize_pollution")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="old_vans")
    y = model.addVar(vtype=GRB.INTEGER, name="new_vans")
    
    # Set objective function: minimize total pollution
    model.setObjective(50*x + 30*y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x + y >= 5000, "min_bottles")
    model.addConstr(y <= 30, "max_new_vans")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal solution
    obj = model.objVal
    
    return obj