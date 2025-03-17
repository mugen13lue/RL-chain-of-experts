import gurobipy as gp
from gurobipy import GRB

def prob_259(escalators, elevators):
    """
    Args:
        escalators: an integer, number of escalators
        elevators: an integer, number of elevators
    Returns:
        obj: an integer, total units of space taken
    """
    m = gp.Model("airport_transportation")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="escalators")
    y = m.addVar(vtype=GRB.INTEGER, name="elevators")

    # Constraints
    m.addConstr(20*x + 8*y >= 400, "Capacity")
    m.addConstr(x >= 3*y, "Escalator_Elevator_Ratio")
    m.addConstr(y >= 2, "Minimum_Elevator")

    # Objective
    m.setObjective(5*x + 2*y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Get the total units of space taken
    obj = m.objVal

    return obj