import gurobipy as gp
from gurobipy import GRB

def prob_262(kayak, motorboat, constraint1):
    """
    Args:
        kayak: an integer representing the number of kayaks to be used
        motorboat: an integer representing the number of motorboats to be used
        constraint1: an integer representing the minimum number of locals to be moved
    Returns:
        obj: an integer representing the amount of time needed to transport all the locals
    """
    m = gp.Model("transportation")

    # Variables
    kayak_trips = m.addVar(name="kayak_trips", vtype=GRB.INTEGER)
    motorboat_trips = m.addVar(name="motorboat_trips", vtype=GRB.INTEGER)

    # Constraints
    m.addConstr(4*kayak_trips + 5*motorboat_trips >= constraint1)
    m.addConstr(5*kayak_trips + 3*motorboat_trips <= 25)
    m.addConstr(kayak_trips >= 0)
    m.addConstr(motorboat_trips >= 0)

    # Objective
    m.setObjective(5*kayak_trips + 3*motorboat_trips, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Return objective value
    return m.objVal