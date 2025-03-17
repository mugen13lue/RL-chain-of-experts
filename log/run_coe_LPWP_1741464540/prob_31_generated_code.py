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
    model = gp.Model("desktop_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="premium_desktops", obj=500)
    y = model.addVar(vtype=GRB.INTEGER, name="regular_desktops", obj=300)

    # Set objective function
    model.setObjective(500*x + 300*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + y <= 200, "production_limit")
    model.addConstr(2000*x + 1000*y <= 300000, "budget_constraint")

    # Set initial values for decision variables based on input arguments
    x.start = premium_desktops
    y.start = regular_desktops

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj