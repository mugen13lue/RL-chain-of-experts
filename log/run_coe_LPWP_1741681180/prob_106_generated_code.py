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
    x1 = model.addVar(vtype=GRB.INTEGER, name="factory_1_hours")
    x2 = model.addVar(vtype=GRB.INTEGER, name="factory_2_hours")

    # Set objective function: minimize the maximum of x1 and x2
    model.setObjective(max_(x1, x2), sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x1 + 10*x2 >= 700, "allergy_pills_constraint")
    model.addConstr(15*x1 + 30*x2 >= 600, "fever_reducing_pills_constraint")
    model.addConstr(20*x1 + 30*x2 <= 1000, "rare_compound_constraint")

    # Optimize the model
    model.optimize()

    # Get the minimum total time needed
    obj = model.objVal

    return obj