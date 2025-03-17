import gurobipy as gp
from gurobipy import GRB

def prob_280():
    """
    Returns:
        obj: an integer, the total number of vehicles
    """
    model = gp.Model("transportation")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of buses
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of personal cars

    # Constraints
    model.addConstr(9*x + 4*y >= 100, "total_children")
    model.addConstr(x >= 5, "more_buses")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj