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
    m = gp.Model("catalyst_optimization")

    # Decision variables
    x = m.addVar(lb=0, vtype=GRB.INTEGER, name="palladium_heavy_catalyst", obj=0)
    y = m.addVar(lb=0, vtype=GRB.INTEGER, name="platinum_heavy_catalyst", obj=0)

    x.setAttr(GRB.Attr.Start, palladium_heavy_catalyst)
    y.setAttr(GRB.Attr.Start, platinum_heavy_catalyst)

    # Constraints
    m.addConstr(15*x + 20*y <= 450, "platinum_constraint")
    m.addConstr(25*x + 14*y <= 390, "palladium_constraint")

    # Objective
    m.setObjective(5*x + 4*y, sense=GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    return int(m.objVal)