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
    obj = 1e9
    
    # Create a new model
    m = gp.Model("transportation")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # number of trips by cargo planes
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # number of trips by ultrawide trucks

    # Set objective function: minimize total number of trips
    m.setObjective(x + y, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(10*x + 6*y >= 200, "transportation_constraint")
    m.addConstr(1000*x + 700*y <= 22000, "cost_constraint")
    m.addConstr(x <= y, "plane_trips_constraint")

    # Optimize model
    m.optimize()

    if m.status == GRB.OPTIMAL:
        obj = m.objVal

    return obj