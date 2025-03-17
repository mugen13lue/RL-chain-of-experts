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

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(0.5*x + 0.7*y >= 4, "Legs")
    model.addConstr(0.8*x + 0.4*y >= 0, "Back")
    model.addConstr(0.3*x + 0.6*y <= 8, "Sleep")

    # Objective
    model.setObjective(0.8*x + 0.4*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    # Get the maximum amount of medicine delivered to the back
    obj = model.objVal

    return obj