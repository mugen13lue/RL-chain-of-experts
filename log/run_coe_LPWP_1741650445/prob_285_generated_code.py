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
    model = gp.Model("trail_design")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of wide trails
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of narrow trails

    # Constraints
    model.addConstr(x <= 3, "trail_capacity")
    model.addConstr(50*x + 20*y <= 225, "visitor_limit")
    model.addConstr(x >= 0, "non_negativity_x")
    model.addConstr(y >= 0, "non_negativity_y")

    # Objective
    model.setObjective(6*x + 3*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the total amount of garbage produced
    obj = model.objVal

    return obj