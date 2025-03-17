import gurobipy as gp
from gurobipy import GRB

def prob_162(bus, car):
    """
    Args:
        bus: an integer (number of bus trips)
        car: an integer (number of car trips)
    
    Returns:
        obj: an integer (total time required to transport the monkeys)
    """
    model = gp.Model("monkey_transportation")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="bus_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="car_trips")

    # Constraints
    model.addConstr(20*x + 6*y >= 300, "monkey_constraint")
    model.addConstr(30*x + 15*y <= GRB.INFINITY, "time_constraint")
    model.addConstr(x <= 10, "bus_trips_constraint")
    model.addConstr(y >= 0.6*x, "car_trips_constraint")

    # Objective
    model.setObjective(30*x + 15*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the total time required
    obj = model.objVal

    return obj