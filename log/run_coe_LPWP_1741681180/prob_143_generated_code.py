import gurobipy as gp
from gurobipy import GRB

def prob_143(large_pill, small_pill):
    """
    Args:
        large_pill: an integer representing the number of large pills
        small_pill: an integer representing the number of small pills

    Returns:
        obj: an integer representing the number of filler material needed
    """
    m = gp.Model("pill_production")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="large_pills")
    y = m.addVar(vtype=GRB.INTEGER, name="small_pills")

    # Constraints
    m.addConstr(3*x + 2*y <= 1000, "medicinal_ingredients")
    m.addConstr(2*x + y <= 1000, "filler_material")
    m.addConstr(x >= 100, "large_pills")
    m.addConstr(y >= 0.6*(x + y), "small_pills")

    # Objective
    m.setObjective(2*x + y, GRB.MINIMIZE)

    m.optimize()

    obj = m.objVal

    return obj