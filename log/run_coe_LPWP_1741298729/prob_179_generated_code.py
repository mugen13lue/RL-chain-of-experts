import gurobipy as gp
from gurobipy import GRB

def prob_179(cargo_planes, ultrawide_trucks):
    """
    Args:
        cargo_planes: an integer, number of cargo planes
        ultrawide_trucks: an integer, number of ultrawide trucks
    Returns:
        obj: an integer, minimum number of trips
    """
    # Create a new model
    model = gp.Model("transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of trips by cargo planes
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of trips by ultrawide trucks

    # Set objective function: minimize total number of trips
    model.setObjective(x + y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x <= 200, "planes_capacity")  # total number of tires transported by planes
    model.addConstr(6*y <= 200, "trucks_capacity")  # total number of tires transported by trucks
    model.addConstr(1000*x + 700*y <= 22000, "cost_constraint")  # total cost constraint
    model.addConstr(x <= y, "plane_trips_constraint")  # constraint on the number of plane trips

    # Optimize the model
    model.optimize()

    # Get the minimum number of trips
    obj = model.objVal

    return obj