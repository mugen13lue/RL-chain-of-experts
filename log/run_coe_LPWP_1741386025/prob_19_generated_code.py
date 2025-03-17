import gurobipy as gp
from gurobipy import GRB

def prob_19():
    """
    Returns:
        obj: an integer, the maximum profit
    """
    m = gp.Model("jar_production")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="thin_jars")
    y = m.addVar(vtype=GRB.INTEGER, name="stubby_jars")

    # Constraints
    m.addConstr(50*x + 30*y <= 3000, "shaping_time")
    m.addConstr(90*x + 150*y <= 4000, "baking_time")

    # Objective
    m.setObjective(5*x + 9*y, sense=GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    return int(m.objVal)