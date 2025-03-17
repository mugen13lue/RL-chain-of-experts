import gurobipy as gp
from gurobipy import GRB

def prob_206(plush_toys, dolls):
    """
    Args:
        plush_toys: an integer representing the number of plush toys
        dolls: an integer representing the number of dolls

    Returns:
        obj: an integer representing the maximum profit
    """
    # Create a new model
    model = gp.Model("toy_store")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="plush_toys")
    y = model.addVar(vtype=GRB.INTEGER, name="dolls")

    # Objective function: maximize profit
    model.setObjective(4*x + 2*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(3*x + 2*y <= 700, "budget_constraint")
    model.addConstr(x >= 90, "min_plush_toys_constraint")
    model.addConstr(x <= 190, "max_plush_toys_constraint")
    model.addConstr(y <= 2*x, "dolls_constraint")

    # Optimize the model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj