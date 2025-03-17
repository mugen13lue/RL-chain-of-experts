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
    x = model.addVar(vtype=GRB.INTEGER, name="regular_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="speed_trips")

    # Set objective function
    model.setObjective(10*x + 20*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 30*y >= mail_to_be_delivered, "mail_pieces")
    model.addConstr(10*x + 20*y <= regular_boat_gas*max_regular_boat_trips, "gas_consumption")
    model.addConstr(x <= max_regular_boat_trips, "regular_boat_trips_limit")
    model.addConstr(y >= 0.5*(x+y), "speed_boat_trips_requirement")
    model.addConstr(y >= 0.5*(x+y), "speed_boat_trips_requirement_2")

    # Optimize the model
    model.optimize()

    # Return the objective value
    return model.objVal