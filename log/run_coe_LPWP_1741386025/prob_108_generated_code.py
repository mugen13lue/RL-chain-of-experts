import gurobipy as gp
from gurobipy import GRB

def prob_108(regular_batch, premium_batch):
    """
    Args:
        regular_batch: an integer, number of regular batches
        premium_batch: an integer, number of premium batches
    Returns:
        obj: an integer, number of people treated
    """
    model = gp.Model("skin_cream_production")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_batches")
    y = model.addVar(vtype=GRB.INTEGER, name="premium_batches")

    # Constraints
    model.addConstr(50*x + 40*y <= 3000)
    model.addConstr(40*x + 60*y <= 3500)
    model.addConstr(x >= 10)
    model.addConstr(x <= y)

    # Objective
    model.setObjective(50*x + 30*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj