import gurobipy as gp
from gurobipy import GRB

def prob_287(x, y, constraint1, constraint2):
    """
    Solves the problem of minimizing the total cost to the hospital.

    Args:
        x: Number of shifts using type II ambulance.
        y: Number of shifts using hospital van.
        constraint1: The constraint that at least 320 patients need to be transported.
        constraint2: The constraint that at most 60% of shifts can be hospital vans.
    
    Returns:
        obj: The objective value representing the total cost.
    """
    
    # Create a new model
    model = gp.Model("hospital_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of shifts using type II ambulance
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of shifts using hospital van

    # Set objective function
    model.setObjective(820*x + 550*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 15*y >= 320, "Patients_Constraint")
    model.addConstr(x + y == x + y, "Shifts_Constraint")
    model.addConstr(x <= 0.6*(x + y), "Ambulance_Constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj