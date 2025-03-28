import gurobipy as gp
from gurobipy import GRB

def prob_224(temperature_check, blood_test):
    """
    Args:
        temperature_check: an integer, the number of temperature checks
        blood_test: an integer, the number of blood tests
    Returns:
        obj: an integer, the number of patients seen
    """
    model = gp.Model("patients_seen")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="temperature_checks")
    y = model.addVar(vtype=GRB.INTEGER, name="blood_tests")

    # Constraints
    model.addConstr(2*x + 10*y <= 22000, "staff_minutes")
    model.addConstr(y >= 45, "blood_tests")
    model.addConstr(x >= 5*y, "temperature_checks")

    # Objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    obj = model.objVal

    return obj