import gurobipy as gp
from gurobipy import GRB

def prob_152(boat, canoe):
    """
    Args:
        boat: an integer, number of trips by boat
        canoe: an integer, number of trips by canoe
    Returns:
        obj: an integer, total amount of time needed to transport the ducks
        boat_trips: an integer, number of boat trips taken
        canoe_trips: an integer, number of canoe trips taken
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

    # Get the total amount of time needed to transport the ducks
    obj = model.objVal

    # Get the number of boat trips and canoe trips taken
    boat_trips = x.x
    canoe_trips = y.x

    return obj, boat_trips, canoe_trips