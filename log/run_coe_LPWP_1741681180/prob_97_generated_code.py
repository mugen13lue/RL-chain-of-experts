from gurobipy import *

def prob_97(premium_model, regular_model):
    """
    Args:
        premium_model: an integer, number of premium printers
        regular_model: an integer, number of regular printers
    Returns:
        objective_value: an integer, total number of printers
    """
    m = Model("printer_optimization")

    # Decision variables
    premium = m.addVar(vtype=GRB.INTEGER, name="premium")
    regular = m.addVar(vtype=GRB.INTEGER, name="regular")

    # Objective function to minimize total number of printers
    m.setObjective(premium + regular, GRB.MINIMIZE)

    # Constraints
    m.addConstr(30 * premium + 20 * regular >= 200, "pages_constraint")
    m.addConstr(4 * premium + 3 * regular <= 35, "ink_constraint")
    m.addConstr(regular <= premium, "user_friendly_constraint")

    # Optimize model
    m.optimize()

    # Return total number of printers
    return int(premium.x + regular.x)