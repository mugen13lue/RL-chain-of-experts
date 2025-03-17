from gurobipy import *

def prob_239(limousine, bus):
    """
    Args:
        limousine: an integer, number of limousines used
        bus: an integer, number of buses used

    Returns:
        obj: an integer, total number of limousines and buses used
    """
    m = Model()

    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="limousines")
    y = m.addVar(vtype=GRB.INTEGER, name="buses")

    # Set objective
    m.setObjective(x + y, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(12*x + 18*y >= 400, "total_people")
    m.addConstr(x >= 0.7*(x + y), "limousine_percentage")

    # Optimize model
    m.optimize()

    # Get the total number of limousines and buses used
    obj = m.objVal

    return obj