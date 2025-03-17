import gurobipy as gp
from gurobipy import GRB

def prob_269(runners, canoers):
    """
    Args:
        runners: an integer, number of runners
        canoers: an integer, number of canoers
    Returns:
        obj: an integer, amount of mail
    """
    model = gp.Model("mail_delivery")

    # Decision Variables
    x = model.addVar(vtype=GRB.INTEGER, name="runners")
    y = model.addVar(vtype=GRB.INTEGER, name="canoers")

    # Constraints
    model.addConstr(x >= 4, "min_runners")
    model.addConstr(x + y <= 50, "total_runners_canoers")
    model.addConstr(3*x + 10*y <= 200, "total_hours")
    model.addConstr(y <= 0.33*(x+y), "canoers_limit")

    # Objective Function
    model.setObjective(3*x + 10*y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj