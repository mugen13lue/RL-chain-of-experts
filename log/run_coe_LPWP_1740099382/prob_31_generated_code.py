from gurobipy import *

def prob_31(premium_desktops, regular_desktops):
    """
    Args:
        premium_desktops: an integer, representing the number of premium desktops
        regular_desktops: an integer, representing the number of regular desktops
    Returns:
        obj: an integer, representing the objective value
        x_opt: an integer, representing the optimal number of premium desktops
        y_opt: an integer, representing the optimal number of regular desktops
    """
    m = Model("desktops")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="premium_desktops")
    y = m.addVar(vtype=GRB.INTEGER, name="regular_desktops")

    # Constraints
    m.addConstr(x + y <= 200, "Production_Limit")
    m.addConstr(2000*x + 1000*y <= 300000, "Budget_Constraint")

    # Objective
    m.setObjective(500*x + 300*y, GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    # Get optimal values
    x_opt = int(x.x)
    y_opt = int(y.x)

    # Return objective value and optimal values
    return int(m.objVal), x_opt, y_opt