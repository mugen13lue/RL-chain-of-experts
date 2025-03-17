import gurobipy as gp
from gurobipy import GRB

def prob_125(anxiety_medication, anti_depressants):
    """
    Args:
        anxiety_medication: an integer (number of units of anxiety medication)
        anti_depressants: an integer (number of units of anti-depressants)
    Returns:
        total_time: an integer (total time it takes for the medication to be effective)
    """
    model = gp.Model("medication_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="anxiety_medication")
    y = model.addVar(vtype=GRB.INTEGER, name="anti_depressants")

    # Constraints
    model.addConstr(x + y >= 100, "min_total_units")
    model.addConstr(x >= 30, "min_anxiety_medication")
    model.addConstr(x <= 2*y, "max_ratio_constraint")

    # Objective
    model.setObjective(3*x + 5*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_time = model.objVal

    return total_time