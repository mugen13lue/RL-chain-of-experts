import gurobipy as gp
from gurobipy import GRB

def prob_251(freight, air):
    """
    Args:
        freight: an integer, number of trips by freight
        air: an integer, number of trips by air
    Returns:
        obj: an integer, total number of trips
    """
    m = gp.Model("transportation")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="freight_trips")
    y = m.addVar(vtype=GRB.INTEGER, name="air_trips")

    # Objective function: minimize total number of trips
    m.setObjective(x + y, GRB.MINIMIZE)

    # Constraints
    m.addConstr(5*x + 3*y >= 200, "min_candles_transported")
    m.addConstr(300*x + 550*y <= 20000, "budget_constraint")
    m.addConstr(y >= 0.3*(x + y), "air_percentage_constraint")
    m.addConstr(x >= 5, "min_freight_trips")

    # Optimize model
    m.optimize()

    obj = m.objVal

    return obj