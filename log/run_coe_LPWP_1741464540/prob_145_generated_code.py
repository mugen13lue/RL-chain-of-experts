import gurobipy as gp
from gurobipy import GRB

def prob_145(process_1, process_2):
    """
    Args:
        process_1: an integer, number of times process 1 should be run
        process_2: an integer, number of times process 2 should be run

    Returns:
        obj: an integer, total time needed to minimize
    """
    model = gp.Model("process_optimization")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # Number of hours process 1 is run
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # Number of hours process 2 is run

    # Constraints
    model.addConstr(50*x + 60*y <= 2000, "preliminary_material_constraint")
    model.addConstr(35*x + 50*y >= 1200, "pain_killer_production_constraint")
    model.addConstr(12*x + 30*y >= 1200, "sleeping_pill_production_constraint")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Return total time needed
    return int(model.objVal)