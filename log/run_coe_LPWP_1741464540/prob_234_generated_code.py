import gurobipy as gp
from gurobipy import GRB

def prob_234():
    """
    Returns:
        total_cost: an integer representing the total cost
    """
    model = gp.Model("workers_scheduling")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="ultrasound_technician_shifts")
    y = model.addVar(vtype=GRB.INTEGER, name="graduate_researcher_shifts")

    # Constraints
    model.addConstr(x >= 2*y)
    model.addConstr(8*x + 5*y == 500)
    model.addConstr(300*x + 100*y <= 14000)

    # Objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    total_cost = model.objVal

    return total_cost