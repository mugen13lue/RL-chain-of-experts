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
    model.addConstr(3*x + 5*y <= 200)
    model.addConstr(y >= 10)
    model.addConstr(x <= 0.3*(x + y))

    # Objective
    model.setObjective(3*x + y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    # Get the total number of tricks performed
    obj = model.objVal

    return obj