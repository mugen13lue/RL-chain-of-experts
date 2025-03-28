import gurobipy as gp
from gurobipy import GRB

def prob_151(ships, planes):
    """
    Args:
        ships: an integer, representing the number of ship trips
        planes: an integer, representing the number of plane trips
    Returns:
        obj: an integer, representing the total amount of fuel consumed
    """
    obj = 0
    
    # Create a new model
    m = gp.Model("transportation_problem")
    
    # Decision variables
    ship_trips = m.addVar(vtype=GRB.INTEGER, name="ship_trips")
    plane_trips = m.addVar(vtype=GRB.INTEGER, name="plane_trips")
    
    # Set objective
    m.setObjective(500*ship_trips + 300*plane_trips, GRB.MINIMIZE)
    
    # Constraints
    m.addConstr(40*ship_trips + 20*plane_trips >= 500, "total_containers_constraint")
    m.addConstr(500*ship_trips <= GRB.INFINITY, "fuel_ships_constraint")
    m.addConstr(300*plane_trips <= GRB.INFINITY, "fuel_planes_constraint")
    m.addConstr(plane_trips <= 10, "max_plane_trips_constraint")
    m.addConstr(ship_trips >= 0.5*(ship_trips+plane_trips), "min_ship_trips_constraint")
    
    # Optimize model
    m.optimize()
    
    # Get the optimal objective value
    obj = m.objVal
    
    return obj