import gurobipy as gp
from gurobipy import GRB

def prob_276():
    """
    Returns:
        obj: an integer, the maximum caloric intake
    """
    model = gp.Model("senior_home")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="spinach")
    y = model.addVar(vtype=GRB.INTEGER, name="soybeans")

    # Constraints
    model.addConstr(100*x + 80*y >= 12000, "fibre")
    model.addConstr(5*x + 12*y >= 300, "iron")
    model.addConstr(x >= y, "spinach_soybeans")

    # Objective
    model.setObjective(30*x + 100*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal) if model.status == GRB.OPTIMAL else None