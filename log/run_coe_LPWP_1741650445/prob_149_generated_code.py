import gurobipy as gp
from gurobipy import GRB

def prob_149(vans, trucks):
    """
    Args:
        vans: an integer, the number of trips by vans
        trucks: an integer, the number of trips by trucks
    Returns:
        obj: an integer, the objective value
    """
    # Create a new model
    model = gp.Model("chocolate_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of trips by vans
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of trips by trucks

    # Set objective function: minimize total number of trips
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 80*y >= 1500, "transportation_constraint")
    model.addConstr(30*x + 50*y <= 1000, "budget_constraint")
    model.addConstr(x >= y, "van_trips_more_than_truck_trips")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj