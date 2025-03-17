import gurobipy as gp
from gurobipy import GRB

def prob_47(bagels, croissants, oven_hours, chef_hours):
    """
    Args:
        bagels: an integer, number of batches of bagels
        croissants: an integer, number of batches of croissants
        oven_hours: an integer, total oven hours used
        chef_hours: an integer, total chef hours used
    Returns:
        obj: an integer, maximum profit
    """
    # Create a new model
    model = gp.Model("bakery")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="bagels")
    y = model.addVar(vtype=GRB.INTEGER, name="croissants")

    # Set objective function
    model.setObjective(20*x + 40*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + y <= oven_hours, "oven_constraint")
    model.addConstr(0.25*x + 2*y <= chef_hours, "chef_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj