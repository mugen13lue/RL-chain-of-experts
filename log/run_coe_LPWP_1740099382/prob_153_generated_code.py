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
    
    # Create a new model
    model = gp.Model("minimize_pollution")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of old vans used
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of new vans used
    
    # Set objective function: minimize pollution
    model.setObjective(50*x + 30*y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(100*x + 80*y >= 5000, "min_bottles_constraint")
    model.addConstr(y <= 30, "max_new_vans_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the total amount of pollution produced
    obj = model.objVal
    
    return obj