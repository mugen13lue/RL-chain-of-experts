from gurobipy import *

def prob_287(type_II_ambulance, hospital_van, constraint1, constraint2):
    """
    Solves the problem of minimizing the total cost to the hospital.

    Args:
        type_II_ambulance: Number of type II ambulances to schedule.
        hospital_van: Number of hospital vans to schedule.
        constraint1: The constraint that at least 320 patients need to be transported.
        constraint2: The constraint that at most 60% of shifts can be hospital vans.
    
    Returns:
        obj: The objective value representing the total cost.
    """
    m = Model("hospital_transportation")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="type_II_ambulance_shifts")
    y = m.addVar(vtype=GRB.INTEGER, name="hospital_van_shifts")

    # Objective function: Minimize Cost
    m.setObjective(820*x + 550*y, GRB.MINIMIZE)

    # Constraints
    m.addConstr(20*x + 15*y >= 320, "patient_requirement")
    m.addConstr(x + y <= 16, "shift_limitation")
    m.addConstr(x <= 0.6*(x + y), "union_limitation")

    # Optimize model
    m.optimize()

    # Get the objective value
    obj = m.objVal

    return obj