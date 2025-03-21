import gurobipy as gp
from gurobipy import GRB

def prob_67(gas, electric):
    """
    Args:
        gas: an integer, number of gas grills
        electric: an integer, number of electric grills
    Returns:
        obj: an integer, minimum number of grills in the store
    """
    model = gp.Model("grill_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="gas_grills")
    y = model.addVar(vtype=GRB.INTEGER, name="electric_grills")

    # Constraints
    model.addConstr(20*x + 30*y >= 150, "cooking_capacity")
    model.addConstr(20*x + 25*y <= 140, "oil_usage")
    model.addConstr(y <= x, "electric_grill_limit")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)