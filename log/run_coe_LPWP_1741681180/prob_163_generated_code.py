import gurobipy as gp
from gurobipy import GRB

def prob_163(helicopters, trucks):
    """
    Args:
        helicopters: an integer, the number of helicopters
        trucks: an integer, the number of trucks
    Returns:
        obj: an integer, the amount of pollution
    """
    m = gp.Model("transportation")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # Number of helicopter trips
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # Number of truck trips

    # Constraints
    m.addConstr(3*x + 7*y >= 80, "cows_constraint")
    m.addConstr(y <= 8, "truck_trips_constraint")

    # Objective
    m.setObjective(5*x + 10*y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Get the amount of pollution
    obj = m.objVal

    return obj