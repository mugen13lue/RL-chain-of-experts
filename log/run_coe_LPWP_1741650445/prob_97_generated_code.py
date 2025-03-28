import gurobipy as gp
from gurobipy import GRB

def prob_97(premium_model, regular_model):
    """
    Args:
        premium_model: an integer, number of premium printers
        regular_model: an integer, number of regular printers
    Returns:
        objective_value: an integer, total number of printers
    """
    m = gp.Model("printer_problem")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="premium_printers")
    y = m.addVar(vtype=GRB.INTEGER, name="regular_printers")

    # Constraints
    m.addConstr(30*x + 20*y >= 200)
    m.addConstr(4*x + 3*y <= 35)
    m.addConstr(y <= x)
    
    # Objective
    m.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    return int(x.x + y.x) if m.status == GRB.OPTIMAL else None