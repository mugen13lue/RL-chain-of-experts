import gurobipy as gp
from gurobipy import GRB

def prob_16(z_tube, soorchle, wassa):
    """
    Args:
        z_tube: an integer representing the number of advertisements on z-tube
        soorchle: an integer representing the number of advertisements on soorchle
        wassa: an integer representing the number of advertisements on wassa

    Returns:
        obj: an integer representing the maximized total audience
    """
    
    # Create a new model
    model = gp.Model("advertisement_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of ads on z-tube
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of ads on soorchle
    z = model.addVar(vtype=GRB.INTEGER, name="z")  # Number of ads on wassa
    
    # Set objective function: maximize total audience
    model.setObjective(400000*x + 5000*y + 3000*z, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(1000*x + 200*y + 100*z <= 10000, "budget_constraint")
    model.addConstr(x >= 0.05*(x + y + z), "viewer_constraint_z_tube")
    model.addConstr(z <= 0.33*(x + y + z), "viewer_constraint_wassa")
    model.addConstr(y <= 15, "limit_on_soorchle_ads")
    
    # Optimize the model
    model.optimize()
    
    # Get the maximized total audience
    obj = int(model.objVal)
    
    return obj