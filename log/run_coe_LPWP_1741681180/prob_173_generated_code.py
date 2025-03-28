from gurobipy import *

def prob_173(van, minibus):
    """
    Args:
        van: an integer, represents the number of vans used
        minibus: an integer, represents the number of minibuses used
    Returns:
        obj: an integer, the total amount of pollution produced
    """
    m = Model("transportation")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="vans")
    y = m.addVar(vtype=GRB.INTEGER, name="minibuses")

    # Constraints
    m.addConstr(6*x + 10*y >= 150, "total_kids_constraint")
    m.addConstr(y <= 10, "minibus_limit_constraint")
    m.addConstr(x >= y, "vans_exceed_minibuses_constraint")

    # Objective
    m.setObjective(7*x + 10*y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    obj = m.objVal

    return obj