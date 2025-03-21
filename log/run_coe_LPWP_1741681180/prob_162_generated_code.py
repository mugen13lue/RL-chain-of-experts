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
    model = gp.Model("monkey_transport")

    # Define decision variables
    x_bus = model.addVar(vtype=GRB.INTEGER, name="bus_trips")
    x_car = model.addVar(vtype=GRB.INTEGER, name="car_trips")

    # Set objective function: minimize total time
    model.setObjective(30*x_bus + 15*x_car, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x_bus <= 10, "bus_limit")
    model.addConstr(0.6*(x_bus + x_car) >= x_car, "car_percentage")
    model.addConstr(20*x_bus + 6*x_car >= 300, "total_monkeys")

    # Optimize the model
    model.optimize()

    # Get the total time required
    obj = model.objVal

    return obj