import gurobipy as gp
from gurobipy import GRB

def prob_171(regular_boats, speed_boats, regular_boat_capacity, regular_boat_gas,
              speed_boat_capacity, speed_boat_gas, max_regular_boat_trips,
              min_speed_boat_trips_percentage, mail_to_be_delivered): 
    """
    Args:
        regular_boats: an integer, number of regular boats
        speed_boats: an integer, number of speed boats
        regular_boat_capacity: an integer, number of mail pieces a regular boat can carry per trip
        regular_boat_gas: an integer, amount of gas (in liters) a regular boat uses per trip
        speed_boat_capacity: an integer, number of mail pieces a speed boat can carry per trip
        speed_boat_gas: an integer, amount of gas (in liters) a speed boat uses per trip
        max_regular_boat_trips: an integer, maximum number of trips a regular boat can make
        min_speed_boat_trips_percentage: a float, minimum percentage of trips that must be made by speed boats
        mail_to_be_delivered: an integer, number of mail pieces to be delivered
    
    Returns:
        objective_value: an integer, the minimum amount of gas consumed
    """
    # Create a new model
    model = gp.Model("mail_delivery")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="regular_boat_trips")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="speed_boat_trips")

    # Set objective function
    model.setObjective(regular_boat_gas*x + speed_boat_gas*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x + y <= max_regular_boat_trips, "max_regular_trips")
    model.addConstr(y >= 0.5*(x + y), "min_speed_trips_percentage")
    model.addConstr(regular_boat_capacity*x + speed_boat_capacity*y >= mail_to_be_delivered, "mail_delivery")

    # Optimize model
    model.optimize()

    # Get the objective value
    objective_value = model.objVal

    return objective_value