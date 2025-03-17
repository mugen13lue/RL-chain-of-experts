import gurobipy as gp
from gurobipy import GRB

def prob_263():
    """
    Returns:
        obj: an integer, the objective value
    """
    model = gp.Model("test_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="blood_tests")
    y = model.addVar(vtype=GRB.INTEGER, name="ear_tests")

    # Constraints
    model.addConstr(30*x + 5*y <= 7525, "time_constraint")
    model.addConstr(x >= 3*y, "blood_test_constraint")
    model.addConstr(y >= 12, "ear_test_constraint")

    # Objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj