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
    model = gp.Model("aquarium_show")

    # Variables
    otters = model.addVar(vtype=GRB.INTEGER, name="otters")
    dolphins = model.addVar(vtype=GRB.INTEGER, name="dolphins")

    # Constraints
    model.addConstr(3*otters + 5*dolphins <= 200, "num_treats")
    model.addConstr(dolphins >= 10, "min_dolphins")
    model.addConstr(otters <= 0.3*(otters + dolphins), "max_otters")

    # Objective
    model.setObjective(3*otters + dolphins, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    obj = int(model.objVal)

    return obj