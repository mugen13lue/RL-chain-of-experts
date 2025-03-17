import gurobipy as gp
from gurobipy import GRB

def prob_145(process_1, process_2):
    """
    Args:
        process_1: an integer, number of times process 1 should be run
        process_2: an integer, number of times process 2 should be run

    Returns:
        obj: an integer, total time needed to minimize
    """
    model = gp.Model("drug_company")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(50*x + 60*y <= 2000, "preliminary_material")
    model.addConstr(35*x + 50*y >= 1200, "min_pain_killers")
    model.addConstr(12*x + 30*y >= 1200, "min_sleeping_pills")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)