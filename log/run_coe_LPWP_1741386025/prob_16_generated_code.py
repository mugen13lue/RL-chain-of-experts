import gurobipy as gp
from gurobipy import GRB

def prob_16(z_tube, soorchle, wassa):
    """
    Args:
        z_tube: an integer representing the number of advertisements on z-tube
        soorchle: an integer representing the number of advertisements on soorchle
        wassa: an integer representing the number of advertisements on wassa

    Returns:
        obj: an integer representing the maximized total audience
    """
    m = gp.Model("advertising")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # Number of ads on z-tube
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # Number of ads on soorchle
    z = m.addVar(vtype=GRB.INTEGER, name="z")  # Number of ads on wassa

    # Objective function: maximize total audience
    m.setObjective(400000*x + 5000*y + 3000*z, sense=GRB.MAXIMIZE)

    # Constraints
    m.addConstr(1000*x + 200*y + 100*z <= 10000, "budget_constraint")
    m.addConstr(x >= 0.05*(x + y + z), "viewer_constraint_ztube")
    m.addConstr(z <= 0.33*(x + y + z), "viewer_constraint_wassa")
    m.addConstr(y <= 15, "limit_soorchle_ads")

    # Optimize model
    m.optimize()

    # Get the maximized total audience
    obj = m.objVal

    return obj