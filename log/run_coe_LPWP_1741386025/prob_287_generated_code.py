import gurobipy as gp
from gurobipy import GRB

def prob_287(type_II_ambulance, hospital_van, constraint1, constraint2):
    """
    Solves the problem of minimizing the total cost to the hospital.

    Args:
        type_II_ambulance: Number of shifts using type II ambulance to schedule.
        hospital_van: Number of shifts using hospital van to schedule.
        constraint1: The constraint that at least 320 patients need to be transported.
        constraint2: The total number of shifts to consider.
    
    Returns:
        obj: The objective value representing the total cost.
    """
    # Create a new model
    model = gp.Model("hospital_transportation")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of shifts using type II ambulance
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of shifts using hospital van

    # Set objective function
    model.setObjective(820*x + 550*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 15*y >= constraint1, "Patients_Constraint")
    model.addConstr(x + y == constraint2, "Shifts_Constraint")
    model.addConstr(x <= 0.6*constraint2, "Ambulance_Constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj