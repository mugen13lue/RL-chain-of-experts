import gurobipy as gp
from gurobipy import GRB

def prob_152():
    """
    Returns:
        obj: an integer, total amount of time needed to transport the ducks
    """
    model = gp.Model("duck_transportation")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="boat_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="canoe_trips")

    # Constraints
    model.addConstr(10*x <= 300, "ducks_transported_by_boat")
    model.addConstr(8*y >= 300, "ducks_transported_by_canoe")
    model.addConstr(x <= 12, "total_boat_trips")
    model.addConstr(y >= 0.6*(x+y), "total_trips_by_canoe")

    # Objective
    model.setObjective(20*x + 40*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Return total amount of time needed
    return int(model.objVal)