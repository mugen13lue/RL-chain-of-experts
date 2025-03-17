import gurobipy as gp
from gurobipy import GRB

def prob_155(otters, dolphins):
    """
    Solve the problem to maximize the total number of tricks that can be performed.

    Args:
        otters: number of otters (integer)
        dolphins: number of dolphins (integer)

    Returns:
        obj: total number of tricks (integer)
    """
    model = gp.Model("maximize_tricks")

    # Decision variables
    otter_tricks = model.addVar(vtype=GRB.INTEGER, name="otter_tricks")
    dolphin_tricks = model.addVar(vtype=GRB.INTEGER, name="dolphin_tricks")

    # Objective function
    model.setObjective(otter_tricks * 3 + dolphin_tricks, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(otter_tricks * 3 + dolphin_tricks * 5 <= 200, "total_treats")
    model.addConstr(otters <= 0.3 * (otters + dolphins), "max_otters")
    model.addConstr(dolphins >= 10, "min_dolphins")

    model.optimize()

    total_tricks = model.objVal

    return total_tricks