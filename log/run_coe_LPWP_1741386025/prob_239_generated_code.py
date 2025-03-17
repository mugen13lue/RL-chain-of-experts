import gurobipy as gp
from gurobipy import GRB

def prob_239(limousine, bus):
    """
    Args:
        limousine: an integer, number of limousines used
        bus: an integer, number of buses used

    Returns:
        obj: an integer, total number of limousines and buses used
    """
    # Create a new model
    model = gp.Model("transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="limousines")
    y = model.addVar(vtype=GRB.INTEGER, name="buses")

    # Set objective: minimize total vehicles used
    model.setObjective(x + y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x + y >= 400, "min_people_constraint")
    model.addConstr(x >= 0, "limousine_non_negative_constraint")
    model.addConstr(y >= 0, "bus_non_negative_constraint")
    model.addConstr(x >= 0.7 * (x + y), "limousine_percentage_constraint")

    # Optimize model
    model.optimize()

    # Get the total number of limousines and buses used
    obj = model.objVal

    return obj