import gurobipy as gp
from gurobipy import GRB

def prob_137():
    """
    Returns:
        obj: an integer, the minimum sugar intake
    """
    model = gp.Model("diet_problem")

    # Variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="oranges")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="grapefruit")

    # Constraints
    model.addConstr(5*x + 7*y >= 80)
    model.addConstr(3*x + 5*y >= 70)
    model.addConstr(x >= 2*y)

    # Objective
    model.setObjective(5*x + 6*y, sense=GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)