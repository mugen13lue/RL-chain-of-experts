import gurobipy as gp
from gurobipy import GRB

def prob_224():
    """
    Returns:
        obj: an integer, the number of patients seen
    """
    # Create a new model
    model = gp.Model("patients_seen")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="temperature_checks")
    y = model.addVar(vtype=GRB.INTEGER, name="blood_tests")

    # Set objective function: maximize the number of patients seen
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + 10*y <= 22000, "staff_minutes")
    model.addConstr(y >= 45, "blood_tests")
    model.addConstr(x >= 5*y, "temperature_checks")

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    obj = model.objVal

    return obj