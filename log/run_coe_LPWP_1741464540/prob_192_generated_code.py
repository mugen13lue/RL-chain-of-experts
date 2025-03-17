import gurobipy as gp
from gurobipy import GRB

def prob_192(helicopter, bus, Min_Patients, Min_Helicopter_Trips, Max_Bus_Trips):
    """
    Args:
        helicopter: an integer, the number of helicopter trips.
        bus: an integer, the number of bus trips.
        Min_Patients: an integer, minimum number of patients to be transported.
        Min_Helicopter_Trips: an integer, minimum number of helicopter trips.
        Max_Bus_Trips: an integer, maximum number of bus trips.

    Returns:
        Total_Time: an integer, the minimum total time to transport the patients.
    """
    m = gp.Model("transportation")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # Number of helicopter trips
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # Number of bus trips

    # Constraints
    m.addConstr(5*x + 8*y >= Min_Patients, "Patients_transported")
    m.addConstr(x >= 0.3*(x+y), "Min_helicopter_trips")
    m.addConstr(y <= Max_Bus_Trips, "Max_bus_trips")

    # Objective
    m.setObjective(x + 3*y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    return int(m.objVal)