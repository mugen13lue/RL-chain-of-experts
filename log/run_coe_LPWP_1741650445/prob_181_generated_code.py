import gurobipy as gp
from gurobipy import GRB

def prob_181():
    """
    Returns:
        obj: an integer, minimum amount of gas used
    """
    model = gp.Model("transportation")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="submarine_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="boat_trips")

    # Constraints
    model.addConstr(100*x + 80*y >= 1000, "mail_constraint")
    model.addConstr(30*x + 25*y <= GRB.INFINITY, "gas_constraint")
    model.addConstr(x <= 6, "submarine_trips_constraint")
    model.addConstr(y >= 0.5*x, "boat_trips_constraint")

    # Objective
    model.setObjective(30*x + 25*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)