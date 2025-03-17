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
    # Create a new model
    model = gp.Model("test_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="blood_tests")
    y = model.addVar(vtype=GRB.INTEGER, name="ear_tests")

    # Set objective function to maximize the number of blood tests
    model.setObjective(x, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x >= 3*y, "blood_test_constraint")
    model.addConstr(y >= 12, "ear_test_constraint")
    model.addConstr(30*x + 5*y <= 7525, "time_constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj