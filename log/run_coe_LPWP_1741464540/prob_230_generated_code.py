import gurobipy as gp
from gurobipy import GRB

def prob_230(calcium_pills, vitamin_d_pills):
    """
    Args:
        calcium_pills: an integer (number of calcium pills)
        vitamin_d_pills: an integer (number of vitamin D pills)
    Returns:
        total_time: an integer (total time for the medication to be effective)
    """
    model = gp.Model("Medication Optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="calcium_pills")
    y = model.addVar(vtype=GRB.INTEGER, name="vitamin_d_pills")

    # Constraints
    model.addConstr(x + y >= 130)
    model.addConstr(y >= 40)
    model.addConstr(x >= y)

    # Objective
    model.setObjective(5*x + 6*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_time = model.objVal

    return total_time