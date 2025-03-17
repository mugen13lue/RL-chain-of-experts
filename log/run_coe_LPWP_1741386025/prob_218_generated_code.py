import gurobipy as gp
from gurobipy import GRB

def prob_218(regular_tacos, deluxe_tacos):
    """
    Args:
        regular_tacos: an integer, the number of regular tacos to make
        deluxe_tacos: an integer, the number of deluxe tacos to make
    Returns:
        obj: an integer, the maximum profit
    """
    model = gp.Model("taco_stand")

    # Variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="regular_tacos")
    x2 = model.addVar(vtype=GRB.INTEGER, name="deluxe_tacos")

    # Objective Function
    model.setObjective(2.50 * x1 + 3.55 * x2, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(x1 <= 50, "regular_tacos_constraint")
    model.addConstr(x2 <= 40, "deluxe_tacos_constraint")
    model.addConstr(x1 + x2 <= 70, "total_tacos_constraint")

    # Optimize model
    model.optimize()

    return model.objVal