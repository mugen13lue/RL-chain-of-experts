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
    # Create a new model
    model = gp.Model("pain_killer_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of doses of pain killer 1
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of doses of pain killer 2

    # Set objective function: maximize amount of medicine delivered to the back
    model.setObjective(0.8*x + 0.4*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(0.5*x + 0.7*y <= 4, "legs_constraint")
    model.addConstr(0.8*x + 0.4*y >= 0, "back_constraint")
    model.addConstr(0.3*x + 0.6*y <= 8, "sleep_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj