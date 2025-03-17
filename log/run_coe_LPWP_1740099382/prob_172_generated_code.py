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
    obj = 1e9
    
    # Create a new model
    m = gp.Model("transportation")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="bus_trips")
    y = m.addVar(vtype=GRB.INTEGER, name="car_trips")

    # Set objective function
    m.setObjective(2*x + 1.5*y, sense=GRB.MINIMIZE)

    # Add constraints
    m.addConstr(100*x + 40*y == 1200, "total_chicken_constraint")
    m.addConstr(x <= 10, "max_bus_trips_constraint")
    m.addConstr(y >= 0.6*(x+y), "min_car_trips_constraint")

    # Optimize model
    m.optimize()

    # Get the optimal objective value
    obj = m.objVal

    return obj