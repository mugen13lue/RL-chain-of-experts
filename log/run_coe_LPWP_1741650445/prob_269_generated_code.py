import gurobipy as gp
from gurobipy import GRB

def prob_269():
    """
    Returns:
        obj: an integer, amount of mail
    """
    model = gp.Model("mail_delivery")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="runners")
    y = model.addVar(vtype=GRB.INTEGER, name="canoers")

    # Constraints
    model.addConstr(x >= 4, "min_runners")
    model.addConstr(3*x + 10*y <= 0.33 * (3*x + 10*y), "canoers_limit")
    model.addConstr(4*x + 2*y <= 200, "total_hours")

    # Objective function
    model.setObjective(3*x + 10*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj