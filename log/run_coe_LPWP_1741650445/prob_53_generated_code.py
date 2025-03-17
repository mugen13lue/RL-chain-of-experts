import gurobipy as gp
from gurobipy import GRB

def prob_53(process_A, process_B):
    """
    Args:
        process_A: an integer,
        process_B: an integer,
    Returns:
        obj: an integer, 
    """
    model = gp.Model("coin_plating")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(3*x + 5*y <= 500, "gold_constraint")
    model.addConstr(2*x + 3*y <= 300, "wire_constraint")

    # Objective
    model.setObjective(5*x + 7*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)