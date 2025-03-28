from gurobipy import *

def prob_285(wide_trail, narrow_trail):
    """
    Args:
        wide_trail: an integer, the number of wide trails
        narrow_trail: an integer, the number of narrow trails
    Returns:
        obj: an integer, the total amount of garbage produced
    """
    m = Model("trail_design")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="wide_trail")
    y = m.addVar(vtype=GRB.INTEGER, name="narrow_trail")

    # Objective function
    m.setObjective(6*x + 3*y, GRB.MINIMIZE)

    # Constraints
    m.addConstr(x >= 0)
    m.addConstr(y >= 0)
    m.addConstr(x <= 3)
    m.addConstr(50*x + 20*y <= 225)

    m.optimize()

    return int(m.objVal)