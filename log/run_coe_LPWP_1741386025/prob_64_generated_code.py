import gurobipy as gp
from gurobipy import GRB

def prob_64(small_container, large_container):
    """
    Args:
        small_container: an integer, number of small containers used
        large_container: an integer, number of large containers used
    Returns:
        obj: an integer, amount of paste produced
    """
    model = gp.Model("pharmaceutical_paste")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="small_container")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="large_container")

    # Constraints
    model.addConstr(10*x + 20*y <= 500, "water_constraint")
    model.addConstr(15*x + 20*y <= 700, "pill_constraint")

    # Objective function
    model.setObjective(20*x + 30*y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    # Return the objective value
    return int(model.objVal)