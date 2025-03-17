import gurobipy as gp
from gurobipy import GRB

def prob_172(bus, car):
    """
    Args:
        bus: an integer
        car: an integer
    Returns:
        obj: an integer
    """
    # Create a new model
    model = gp.Model("chicken_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="bus_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="car_trips")

    # Set objective function
    model.setObjective(2*x + 1.5*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x <= 10, "max_bus_trips")
    model.addConstr(x + y >= 0.6 * (x + y), "min_car_trips")
    model.addConstr(100*x + 40*y >= 1200, "total_chicken")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj