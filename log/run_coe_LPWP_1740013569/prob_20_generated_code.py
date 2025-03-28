from gurobipy import *

def prob_20(banana_haters_package, combo_package):
    """
    Args:
        banana_haters_package: an integer representing the quantity of banana-haters packages
        combo_package: an integer representing the quantity of combo packages
    Returns:
        obj: an integer representing the maximum net profit
    """
    m = Model("Grocery_Store_Profit")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="banana_haters_packages")
    y = m.addVar(vtype=GRB.INTEGER, name="combo_packages")

    # Constraints
    m.addConstr(6*x + 5*y <= 10, "apples_constraint")
    m.addConstr(6*y <= 20, "bananas_constraint")
    m.addConstr(30*x + 20*y <= 80, "grapes_constraint")

    # Objective function
    m.setObjective(6*x + 7*y, GRB.MAXIMIZE)

    # Solve the model
    m.optimize()

    return int(m.objVal)