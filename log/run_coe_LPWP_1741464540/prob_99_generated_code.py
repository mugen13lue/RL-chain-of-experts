import gurobipy as gp
from gurobipy import GRB

def prob_99(peach_flavored_candy, cherry_flavored_candy):
    """
    Args:
        peach_flavored_candy: an integer, the number of peach flavored candy packs
        cherry_flavored_candy: an integer, the number of cherry flavored candy packs

    Returns:
        obj: an integer, the minimal amount of special syrup used
    """
    m = gp.Model("candy_production")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="peach_candy")
    y = m.addVar(vtype=GRB.INTEGER, name="cherry_candy")

    # Constraints
    m.addConstr(3*x <= 3000, "peach_flavoring")
    m.addConstr(5*y <= 4000, "cherry_flavoring")
    m.addConstr(x >= y, "peach_popular")
    m.addConstr(y >= 0.3*(x+y), "at_least_30_percent_cherry")

    # Objective
    m.setObjective(5*x + 4*y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    return int(m.objVal)