import gurobipy as gp
from gurobipy import GRB

def prob_149(vans, trucks):
    """
    Args:
        vans: an integer, the number of trips by vans
        trucks: an integer, the number of trips by trucks
    Returns:
        obj: an integer, the objective value
    """
    m = gp.Model("transportation")

    # Decision variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="x")  # number of trips by vans
    y = m.addVar(vtype=GRB.CONTINUOUS, name="y")  # number of trips by trucks

    # Constraints
    m.addConstr(x >= 0)
    m.addConstr(y >= 0)
    m.addConstr(50*x + 80*y >= 1500)
    m.addConstr(30*x + 50*y <= 1000)
    m.addConstr(x >= y)

    # Objective function
    m.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    obj = m.objVal

    return obj