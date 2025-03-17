import gurobipy as gp
from gurobipy import GRB

def prob_139():
    """
    Returns:
        obj: an integer, the objective value
    """
    model = gp.Model("virus_testing")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="spit_tests")
    y = model.addVar(vtype=GRB.INTEGER, name="swabs")

    # Constraints
    model.addConstr(10*x + 15*y <= 8000, "time_constraint")
    model.addConstr(x >= 2*y, "spit_test_constraint")
    model.addConstr(y >= 20, "swab_test_constraint")

    # Objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj