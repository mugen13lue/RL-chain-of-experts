import gurobipy as gp
from gurobipy import GRB

def prob_106(x_hours, y_hours):
    """
    Args:
        x_hours: an integer, number of hours factory 1 should be run
        y_hours: an integer, number of hours factory 2 should be run

    Returns:
        obj: an integer, the minimum total time needed
    """
    model = gp.Model("factory_optimization")

    # Define variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # hours factory 1 is run
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # hours factory 2 is run

    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 30*y <= 1000, "rare_compound_constraint")
    model.addConstr(20*x + 10*y >= 700, "allergy_pills_constraint")
    model.addConstr(15*x + 30*y >= 600, "fever_reducing_pills_constraint")

    # Optimize model
    model.optimize()

    return int(model.objVal)  # Return the minimum total time needed