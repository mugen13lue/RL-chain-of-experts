import gurobipy as gp
from gurobipy import GRB

def prob_143(large_pill, small_pill):
    """
    Args:
        large_pill: an integer representing the number of large pills
        small_pill: an integer representing the number of small pills

    Returns:
        obj: an integer representing the number of filler material needed
    """
    model = gp.Model("pill_production")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of large pills
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of small pills

    # Constraints
    model.addConstr(3*x + 2*y <= 1000, "medicinal_ingredients_constraint")
    model.addConstr(2*x + y <= 1000, "filler_material_constraint")
    model.addConstr(x >= 100, "large_pills_constraint")
    model.addConstr(y >= 0.6*(x + y), "small_pills_constraint")

    # Objective
    model.setObjective(2*x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)  # Return the objective value