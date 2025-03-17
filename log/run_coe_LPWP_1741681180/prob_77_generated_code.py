import gurobipy as gp
from gurobipy import GRB

def prob_77(dual, single):
    """
    Args:
        dual: an integer, representing the number of dual model stamping machines
        single: an integer, representing the number of single model stamping machines
    Returns:
        obj: an integer, representing the total number of stamping machines
    """
    m = gp.Model("stamp_machines")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="dual_machines")
    y = m.addVar(vtype=GRB.INTEGER, name="single_machines")

    # Constraints
    m.addConstr(50*x + 30*y >= 300)
    m.addConstr(20*x + 15*y <= 135)
    m.addConstr(y >= x)

    # Objective
    m.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    return int(x.x), int(y.x)