import gurobipy as gp
from gurobipy import GRB

def prob_64():
    """
    Returns:
        obj: an integer, amount of paste produced
    """
    model = gp.Model("pharmaceutical_paste")

    # Variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="small_containers")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="large_containers")

    # Constraints
    model.addConstr(10*x + 20*y <= 500, "water_constraint")
    model.addConstr(15*x + 20*y <= 700, "powdered_pill_constraint")

    # Objective
    model.setObjective(20*x + 30*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj