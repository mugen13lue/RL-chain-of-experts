import gurobipy as gp
from gurobipy import GRB

def prob_84(experiment_alpha, experiment_beta):
    """
    Args:
        experiment_alpha: an integer, represents the number of times to conduct experiment alpha
        experiment_beta: an integer, represents the number of times to conduct experiment beta
    Returns:
        obj: an integer, the maximum amount of electricity produced
    """
    model = gp.Model("electricity_production")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(3*x + 5*y <= 800, "metal_constraint")
    model.addConstr(5*x + 4*y <= 750, "acid_constraint")

    # Objective function
    model.setObjective(8*x + 10*y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj