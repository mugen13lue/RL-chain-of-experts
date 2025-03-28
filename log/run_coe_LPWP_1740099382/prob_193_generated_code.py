import gurobipy as gp
from gurobipy import GRB

def prob_193(car, bus, constraint1, constraint2):
    """
    Args:
        car: number of cars (integer)
        bus: number of buses (integer)
        constraint1: value of the first constraint (integer)
        constraint2: value of the second constraint (integer)
    Returns:
        obj: the objective value (integer)
    """
    # Create a new model
    model = gp.Model("transport_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of cars
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of buses

    # Set objective function
    model.setObjective(10*x + 30*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(4*x + 20*y >= constraint1, "Transport_Capacity")
    model.addConstr(y <= constraint2, "Bus_Limit")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj