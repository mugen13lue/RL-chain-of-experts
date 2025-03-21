import gurobipy as gp
from gurobipy import GRB

def prob_69(brownies, lemon_squares):
    """
    Args:
        brownies: an integer, the number of brownies to be made
        lemon_squares: an integer, the number of lemon squares to be made
        
    Returns:
        obj: an integer, the total amount of fiber needed
    """
    model = gp.Model("Bakery")

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="brownies")
    x2 = model.addVar(vtype=GRB.INTEGER, name="lemon_squares")

    # Objective function: minimize total amount of fiber
    model.setObjective(4*x1 + 6*x2, GRB.MINIMIZE)

    # Constraints
    model.addConstr(5*x1 + 7*x2 <= 2500, "chocolate_mix")
    model.addConstr(4*x1 + 6*x2 <= 3300, "lemon_mix")
    model.addConstr(x1 <= 0.4*(x1 + x2), "brownies_percentage")

    model.optimize()

    obj = model.objVal

    return obj