import gurobipy as gp
from gurobipy import GRB

def prob_178(bike, car):
    """
    Args:
        bike: an integer, represents the number of bikes
        car: an integer, represents the number of cars
    Returns:
        obj: an integer, the objective value
    """
    obj = 1e9

    # Create a new model
    model = gp.Model("transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="cars")
    y = model.addVar(vtype=GRB.INTEGER, name="bikes")

    # Set objective function: minimize the total number of bikes needed
    model.setObjective(y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x + y >= 100, "min_people")
    model.addConstr(5*x + 3*y >= 500, "min_transport")
    model.addConstr(x <= 0.4*(x + y), "max_cars")

    # Optimize the model
    model.optimize()

    if model.status == GRB.OPTIMAL:
        obj = model.objVal

    return obj