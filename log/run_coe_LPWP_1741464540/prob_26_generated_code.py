import gurobipy as gp
from gurobipy import GRB

def prob_26(Zodiac, Sunny):
    """
    Args:
        Zodiac: an integer, number of pills of Zodiac
        Sunny: an integer, number of pills of Sunny
    Returns:
        obj: an integer, objective value
    """
    # Create a new LP model
    model = gp.Model("medicine_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of pills of Zodiac
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of pills of Sunny

    # Set objective function: Minimize Cost
    model.setObjective(Zodiac * x + Sunny * y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(1.3 * x + 1.2 * y >= 5, "Z1_requirement")
    model.addConstr(1.5 * x + 5 * y >= 10, "D3_requirement")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj