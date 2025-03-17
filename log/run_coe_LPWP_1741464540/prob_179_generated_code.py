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
    m = gp.Model("transportation")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # Number of trips by cargo planes
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # Number of trips by ultrawide trucks

    # Constraints
    m.addConstr(10*x + 6*y >= 200, "tires_constraint")
    m.addConstr(1000*x + 700*y <= 22000, "cost_constraint")
    m.addConstr(x <= y, "plane_trips_constraint")

    # Objective
    m.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    obj = m.objVal

    return obj