import gurobipy as gp
from gurobipy import GRB

def prob_130(pain_killer_1, pain_killer_2):
    """
    Args:
        pain_killer_1: an integer, number of doses of pain killer 1
        pain_killer_2: an integer, number of doses of pain killer 2

    Returns:
        obj: an integer, maximum amount of medicine delivered to the back
    """
    model = gp.Model("pain_killer_optimization")

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="x1")  # Number of doses of pain killer 1
    x2 = model.addVar(vtype=GRB.INTEGER, name="x2")  # Number of doses of pain killer 2

    # Objective function: maximize the amount of medicine delivered to the back
    model.setObjective(0.8*x1 + 0.4*x2, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(0.5*x1 + 0.7*x2 >= 4, "legs_constraint")  # At least 4 units of medicine to the legs
    model.addConstr(0.3*x1 + 0.6*x2 <= 8, "sleep_constraint")  # At most 8 units of sleep medicine

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj