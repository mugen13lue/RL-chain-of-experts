import gurobipy as gp
from gurobipy import GRB

def prob_31(premium_desktops, regular_desktops):
    """
    Args:
        premium_desktops: an integer, representing the number of premium desktops
        regular_desktops: an integer, representing the number of regular desktops
    Returns:
        obj: an integer, representing the objective value
    """
    
    # Create a new model
    model = gp.Model("desktops_production")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="premium_desktops")
    y = model.addVar(vtype=GRB.INTEGER, name="regular_desktops")
    
    # Set objective function
    model.setObjective(500*x + 300*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(2000*x + 1000*y <= 300000, "total_cost_constraint")
    model.addConstr(x + y <= 200, "total_number_constraint")
    model.addConstr(x >= 0, "non_negativity_premium")
    model.addConstr(y >= 0, "non_negativity_regular")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj