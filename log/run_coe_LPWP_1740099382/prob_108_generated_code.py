import gurobipy as gp
from gurobipy import GRB

def prob_108():
    """
    Returns:
        obj: an integer, number of people treated
    """
    model = gp.Model("skin_cream_batches")

    # Variables
    regular_batches = model.addVar(vtype=GRB.INTEGER, name="regular_batches")
    premium_batches = model.addVar(vtype=GRB.INTEGER, name="premium_batches")

    # Constraints
    model.addConstr(50 * regular_batches + 40 * premium_batches <= 3000)
    model.addConstr(40 * regular_batches + 60 * premium_batches <= 3500)
    model.addConstr(regular_batches >= 10)
    model.addConstr(regular_batches <= premium_batches)

    # Objective
    model.setObjective(50 * regular_batches + 30 * premium_batches, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    # Return optimal objective value
    return int(model.objVal)