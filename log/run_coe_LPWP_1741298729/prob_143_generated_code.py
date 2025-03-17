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
    m = gp.Model("pill_production")

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # number of large pills
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # number of small pills

    # Constraints
    m.addConstr(3*x + 2*y <= 1000, "medicinal_ingredients_constraint")
    m.addConstr(2*x + y <= 1000, "filler_constraint")
    m.addConstr(x >= 100, "minimum_large_pills_constraint")
    m.addConstr(y >= 0.6*(x + y), "minimum_small_pills_constraint")

    # Objective
    m.setObjective(2*x + y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Return objective value
    return m.objVal