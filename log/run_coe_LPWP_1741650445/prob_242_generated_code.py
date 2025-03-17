import gurobipy as gp
from gurobipy import GRB

def prob_242(salmon, eggs):
    """
    Args:
        salmon: an integer, the number of bowls of salmon to eat
        eggs: an integer, the number of bowls of eggs to eat
    Returns:
        obj: a float, the objective value (sodium intake)
    """
    model = gp.Model("FitnessGuru")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="salmon")
    y = model.addVar(vtype=GRB.INTEGER, name="eggs")

    # Set objective function: minimize sodium intake
    model.setObjective(80*x + 20*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(300*x + 200*y >= 2000, "Calories")
    model.addConstr(15*x + 8*y >= 90, "Protein")
    model.addConstr(y <= 0.4*x, "MaximumEggLimit")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj