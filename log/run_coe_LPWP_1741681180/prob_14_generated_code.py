import gurobipy as gp
from gurobipy import GRB

def prob_14(long, short_cables, constraint1, constraint2, constraint3):
    """
    Args:
        long: an integer, the number of long cables
        short_cables: an integer, the number of short cables
        constraint1: an integer, the value of the first constraint
        constraint2: an integer, the value of the second constraint
        constraint3: an integer, the value of the third constraint

    Returns:
        obj: an integer, the objective value
    """
    m = gp.Model("cable_problem")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="long_cables")
    y = m.addVar(vtype=GRB.INTEGER, name="short_cables")

    # Objective function
    m.setObjective(12*x + 5*y, sense=GRB.MAXIMIZE)

    # Constraints
    m.addConstr(10*x + 7*y <= 1000, "gold_constraint")
    m.addConstr(y >= 5*x, "short_long_ratio_constraint")
    m.addConstr(x >= 10, "min_long_cables_constraint")

    m.optimize()

    return int(m.objVal)