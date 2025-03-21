import gurobipy as gp
from gurobipy import GRB

def prob_106(factory_1, factory_2):
    """
    Args:
        factory_1: an integer, number of hours factory 1 should be run
        factory_2: an integer, number of hours factory 2 should be run

    Returns:
        obj: an integer, the minimum total time needed
    """
    # Create a new model
    model = gp.Model("factory_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="factory_1_hours")
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="factory_2_hours")

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 30*y <= 1000, "rare_compound_constraint")
    model.addConstr(20*x + 10*y >= 700, "allergy_pills_constraint")
    model.addConstr(15*x + 30*y >= 600, "fever_reducing_pills_constraint")

    # Optimize model
    model.optimize()

    # Get the minimum total time needed
    obj = model.objVal

    return obj