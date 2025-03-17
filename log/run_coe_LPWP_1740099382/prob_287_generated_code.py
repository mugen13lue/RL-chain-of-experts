import gurobipy as gp
from gurobipy import GRB

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
    # Create a new model
    model = gp.Model("hospital_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="num_type_II_ambulance_shifts")  # Number of shifts using type II ambulance
    y = model.addVar(vtype=GRB.INTEGER, name="num_hospital_van_shifts")  # Number of shifts using hospital van

    # Set objective function: Minimize total cost
    model.setObjective(820*x + 550*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 15*y >= 320, "patients_constraint")
    model.addConstr(x + y == type_II_ambulance + hospital_van, "shifts_constraint")
    model.addConstr(x <= 0.6*(type_II_ambulance + hospital_van), "ambulance_constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj