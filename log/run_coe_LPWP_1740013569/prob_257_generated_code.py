import gurobipy as gp
from gurobipy import GRB

def prob_257(palladium_heavy_catalyst, platinum_heavy_catalyst):
    """
    Args:
        palladium_heavy_catalyst (int): The number of palladium-heavy catalyst to be used.
        platinum_heavy_catalyst (int): The number of platinum-heavy catalyst to be used.

    Returns:
        obj (int): The maximum amount converted into carbon dioxide.
    """
    model = gp.Model("catalyst_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="palladium_heavy_catalyst")
    y = model.addVar(vtype=GRB.INTEGER, name="platinum_heavy_catalyst")

    # Constraints
    model.addConstr(15*x + 20*y <= 450, "platinum_constraint")
    model.addConstr(25*x + 14*y <= 390, "palladium_constraint")

    # Objective
    model.setObjective(5*x + 4*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)