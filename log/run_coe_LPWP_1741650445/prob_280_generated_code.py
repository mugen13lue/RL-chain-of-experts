import gurobipy as gp
from gurobipy import GRB

def prob_280(bus, personal_car):
    """
    Args:
        bus: an integer, represents the number of buses
        personal_car: an integer, represents the number of personal cars
    Returns:
        obj: an integer, the total number of vehicles
    """
    model = gp.Model("transportation")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of buses
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of personal cars

    # Constraints
    model.addConstr(9*x + 4*y >= 100, "total_children")
    model.addConstr(x >= 5, "more_buses")
    
    # Integer constraints
    model.addConstr(x, GRB.INTEGER, name="int_constraint_x")
    model.addConstr(y, GRB.INTEGER, name="int_constraint_y")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj