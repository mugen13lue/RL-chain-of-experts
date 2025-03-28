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
    # Create a new model
    model = gp.Model("catalyst_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="palladium_heavy_catalyst")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="platinum_heavy_catalyst")

    # Set objective function
    model.setObjective(5*palladium_heavy_catalyst + 4*platinum_heavy_catalyst, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(15*palladium_heavy_catalyst + 20*platinum_heavy_catalyst <= 450, "platinum_constraint")
    model.addConstr(25*palladium_heavy_catalyst + 14*platinum_heavy_catalyst <= 390, "palladium_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj