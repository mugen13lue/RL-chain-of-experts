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

    # Decision Variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="palladium_heavy_catalyst")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="platinum_heavy_catalyst")

    # Constraints
    platinum_constraint = model.addConstr(15*x + 20*y <= 450, "platinum_constraint")
    palladium_constraint = model.addConstr(25*x + 14*y <= 390, "palladium_constraint")

    # Objective Function
    model.setObjective(5*x + 4*y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    # Return the objective value
    return int(model.objVal) if model.status == GRB.OPTIMAL else 0