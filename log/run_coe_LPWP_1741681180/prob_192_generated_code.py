import gurobipy as gp
from gurobipy import GRB

def prob_192(helicopter_trips, bus_trips, Min_Patients, Min_Helicopter_Trips, Max_Bus_Trips):
    """
    Args:
        helicopter_trips: an integer, the number of helicopter trips.
        bus_trips: an integer, the number of bus trips.
        Min_Patients: an integer, minimum number of patients to be transported.
        Min_Helicopter_Trips: an integer, minimum number of helicopter trips.
        Max_Bus_Trips: an integer, maximum number of bus trips.

    Returns:
        Total_Time: an integer, the minimum total time to transport the patients.
    """
    m = gp.Model("transportation")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="helicopter_trips")  # number of helicopter trips
    y = m.addVar(vtype=GRB.INTEGER, name="bus_trips")  # number of bus trips

    # Objective function: minimize total time
    m.setObjective(x + 3*y, GRB.MINIMIZE)

    # Constraints
    m.addConstr(5*x + 8*y >= Min_Patients, "min_patients_constraint")
    m.addConstr(x >= Min_Helicopter_Trips, "min_helicopter_trips_constraint")
    m.addConstr(y <= Max_Bus_Trips, "max_bus_trips_constraint")

    # Optimize model
    m.optimize()

    # Get total time
    Total_Time = m.objVal

    return Total_Time