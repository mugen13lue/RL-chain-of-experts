import gurobipy as gp
from gurobipy import GRB

def prob_31():
    """
    Returns:
        obj: an integer, representing the objective value
    """
    # Create a new model
    model = gp.Model("desktop_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="premium_desktops")
    y = model.addVar(vtype=GRB.INTEGER, name="regular_desktops")

    # Set objective function
    model.setObjective(500*x + 300*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + y <= 200, "production_limit")
    model.addConstr(2000*x + 1000*y <= 300000, "budget_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj