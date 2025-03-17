import gurobipy as gp
from gurobipy import GRB

def prob_21(bread, cookies):
    """
    This function solves the given problem to maximize total profit.

    Args:
        bread: The number of loaves of bread to bake.
        cookies: The number of batches of cookies to bake.

    Returns:
        obj: The maximum total profit.
    """
    # Create a new model
    model = gp.Model("bakery")

    # Create variables
    x = model.addVar(vtype=GRB.INTEGER, name="bread")
    y = model.addVar(vtype=GRB.INTEGER, name="cookies")

    # Set objective function
    model.setObjective(5*x + 3*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + 0.5*y <= 3000, "stand_mixer_hours")
    model.addConstr(3*x + y <= 3000, "oven_hours")

    # Optimize model
    model.optimize()

    # Get the maximum total profit
    obj = model.objVal

    return obj