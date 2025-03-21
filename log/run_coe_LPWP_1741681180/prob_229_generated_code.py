import gurobipy as gp
from gurobipy import GRB

def prob_229(low_power, high_power):
    """
    Solves the air conditioner problem.

    Args:
        low_power: an integer, number of low-powered air conditioners
        high_power: an integer, number of high-powered air conditioners

    Returns:
        obj: an integer, total number of air conditioners
    """
    m = gp.Model("air_conditioner_problem")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")
    y = m.addVar(vtype=GRB.INTEGER, name="y")

    # Objective function: minimize total number of air conditioners
    m.setObjective(x + y, GRB.MINIMIZE)

    # Constraints
    m.addConstr(12*x + 17*y >= 250, "cooling_capacity")
    m.addConstr(150*x + 250*y <= 3400, "electricity_constraint")
    m.addConstr(x <= 0.3*(x + y), "low_power_limit")
    m.addConstr(y >= 7, "high_power_limit")

    m.optimize()

    obj = m.objVal

    return obj