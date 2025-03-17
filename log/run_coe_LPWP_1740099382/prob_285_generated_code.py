import gurobipy as gp
from gurobipy import GRB

def prob_285(wide_trail, narrow_trail):
    """
    Args:
        wide_trail: an integer, the number of wide trails
        narrow_trail: an integer, the number of narrow trails
    Returns:
        obj: an integer, the total amount of garbage produced
    """
    
    # Create a new model
    model = gp.Model("trail_design")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of wide trails
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of narrow trails
    
    # Set objective function
    model.setObjective(6*x + 3*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x <= 3, "wide_trail_constraint")
    model.addConstr(x + y <= 225, "visitor_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the total amount of garbage produced
    obj = model.objVal
    
    return obj