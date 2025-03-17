import gurobipy as gp
from gurobipy import GRB

def prob_234(ultrasound_technicians, graduate_researchers):
    """
    Args:
        ultrasound_technicians: an integer representing the number of ultrasound technicians
        graduate_researchers: an integer representing the number of graduate researchers
    Returns:
        total_cost: an integer representing the total cost
    """
    model = gp.Model("workers_scheduling")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="ultrasound_technician_shifts")
    y = model.addVar(vtype=GRB.INTEGER, name="graduate_researcher_shifts")

    # Constraints
    model.addConstr(8*x + 5*y >= 500, "shift_hours_constraint")
    model.addConstr(300*x + 100*y <= 14000, "budget_constraint")
    model.addConstr(x >= 2*y, "technician_researcher_ratio_constraint")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_cost = model.objVal

    return total_cost