import gurobipy as gp
from gurobipy import GRB

def prob_115(fertilizer, seeds):
    """
    Args:
        fertilizer: an integer, the number of units of fertilizer
        seeds: an integer, the number of units of seeds
    Returns:
        obj: an integer, the total time it takes for the lawn to be ready
    """
    m = gp.Model("lawn_optimization")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="fertilizer")
    y = m.addVar(vtype=GRB.INTEGER, name="seeds")

    # Constraints
    m.addConstr(x + y <= 300, "total_units_constraint")
    m.addConstr(x >= 50, "min_fertilizer_constraint")
    m.addConstr(x <= 2*y, "max_ratio_constraint")

    # Objective
    m.setObjective(0.5*x + 1.5*y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Get the total time it takes for the lawn to be ready
    obj = m.objVal

    return obj