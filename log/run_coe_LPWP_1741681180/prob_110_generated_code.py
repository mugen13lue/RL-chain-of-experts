from gurobipy import *

def prob_110(syrup_1, syrup_2):
    """
    Args:
        syrup_1: a float, the number of servings of syrup 1
        syrup_2: a float, the number of servings of syrup 2
    Returns:
        obj: a float, the objective value (sugar intake)
    """
    m = Model("syrup_optimization")

    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")
    y = m.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective
    m.setObjective(0.5*x + 0.3*y, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(0.5*x + 0.2*y >= 5)
    m.addConstr(0.4*x + 0.5*y >= 4)
    m.addConstr(x >= 0)
    m.addConstr(y >= 0)

    # Optimize model
    m.optimize()

    # Get objective value
    obj = m.objVal

    return obj