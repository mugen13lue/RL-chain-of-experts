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
    model = gp.Model("Ultrasound Scheduling")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="ultrasound_technicians")
    y = model.addVar(vtype=GRB.INTEGER, name="graduate_researchers")

    # Objective function
    model.setObjective(300*x + 100*y, GRB.MINIMIZE)

    # Constraints
    model.addConstr(x >= 2*y)
    model.addConstr(8*x + 5*y >= 500)
    model.addConstr(300*x + 100*y <= 14000)

    # Optimize model
    model.optimize()

    total_cost = model.objVal

    return total_cost