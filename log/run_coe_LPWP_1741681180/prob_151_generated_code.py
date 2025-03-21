from gurobipy import *

def prob_151(ships, planes):
    """
    Args:
        ships: an integer, representing the number of ship trips
        planes: an integer, representing the number of plane trips
    Returns:
        obj: an integer, representing the total amount of fuel consumed
    """
    m = Model("transportation")

    ship_capacity = 40
    ship_fuel = 500
    plane_capacity = 20
    plane_fuel = 300

    ship_trips = m.addVar(vtype=GRB.INTEGER, name="ship_trips")
    plane_trips = m.addVar(vtype=GRB.INTEGER, name="plane_trips")

    m.setObjective(ship_fuel * ship_trips + plane_fuel * plane_trips, GRB.MINIMIZE)

    m.addConstr(ship_capacity * ship_trips + plane_capacity * plane_trips >= 500, "min_containers")
    m.addConstr(plane_trips <= 10, "max_plane_trips")
    m.addConstr(ship_trips >= 0.5 * (ship_trips + plane_trips), "min_ship_trips")

    m.optimize()

    total_fuel = m.objVal

    return total_fuel