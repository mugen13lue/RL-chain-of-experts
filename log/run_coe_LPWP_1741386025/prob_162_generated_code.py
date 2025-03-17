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
    # Create a new model
    model = gp.Model("monkey_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="bus_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="car_trips")

    # Set objective function: minimize total time
    model.setObjective(30*x + 15*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 6*y >= 300, "monkey_constraint")
    model.addConstr(0.6*x <= y, "car_trips_constraint")
    model.addConstr(x <= 10, "bus_trips_constraint")

    # Optimize model
    model.optimize()

    # Get the total time required
    obj = model.objVal

    return obj