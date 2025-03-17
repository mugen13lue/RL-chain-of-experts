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
    model = gp.Model("aquarium_tricks")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="otters")
    y = model.addVar(vtype=GRB.INTEGER, name="dolphins")

    # Constraints
    model.addConstr(3*x + 5*y <= 200, "num_treats")
    model.addConstr(y >= 10, "min_dolphins")
    model.addConstr(x <= 0.3*(x+y), "max_otters")

    # Objective
    model.setObjective(3*x + y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    # Get the total number of tricks
    obj = int(model.objVal)

    return obj