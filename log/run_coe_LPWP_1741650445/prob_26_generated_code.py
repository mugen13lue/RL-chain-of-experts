import gurobipy as gp
from gurobipy import GRB

def prob_26():
    """
    Returns:
        obj: an integer, objective value
    """
    model = gp.Model("medicine_optimization")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(1.3*x + 1.2*y >= 5, "Z1_requirement")
    model.addConstr(1.5*x + 5*y >= 10, "D3_requirement")

    # Objective function
    model.setObjective(x + 3*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj