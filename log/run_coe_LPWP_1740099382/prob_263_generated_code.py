import gurobipy as gp
from gurobipy import GRB

def prob_263(ear, blood):
    """
    Args:
        ear: an integer, the number of ear tests
        blood: an integer, the number of blood tests

    Returns:
        obj: an integer, the objective value
    """
    obj = 0

    # Create a new model
    model = gp.Model("test_allocation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="blood_tests")
    y = model.addVar(vtype=GRB.INTEGER, name="ear_tests")

    # Set objective function
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(30*x <= 7525, "blood_test_time")
    model.addConstr(5*y <= 7525, "ear_test_time")
    model.addConstr(x >= 3*y, "blood_test_requirement")
    model.addConstr(y >= 12, "ear_test_requirement")

    # Optimize the model
    model.optimize()

    if model.status == GRB.OPTIMAL:
        obj = model.objVal

    return obj