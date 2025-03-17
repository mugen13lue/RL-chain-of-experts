import gurobipy as gp
from gurobipy import GRB

def prob_116(factory_1, factory_2, base_gel):
    """
    Args:
        factory_1: an integer, units of acne cream produced by factory 1 per hour
        factory_2: an integer, units of acne cream produced by factory 2 per hour
        base_gel: an integer, units of base gel required by both factories per hour
    Returns:
        total_time: an integer, total time needed to minimize the total time
    """
    model = gp.Model("factory_optimization")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # Hours factory 1 is run
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # Hours factory 2 is run

    # Constraints
    model.addConstr(12*x + 20*y >= 800, "acne_cream_production")
    model.addConstr(15*x + 10*y >= 1000, "anti_bacterial_cream_production")
    model.addConstr(30*x + 45*y <= 5000, "base_gel_availability")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_time = model.objVal

    return total_time