import gurobipy as gp
from gurobipy import GRB

def prob_137(oranges, grapefruit):
    """
    Args:
        oranges: an integer, the number of oranges to eat
        grapefruit: an integer, the number of grapefruit to eat
    Returns:
        obj: an integer, the minimum sugar intake
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="oranges")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="grapefruit")

    # Set objective function: minimize sugar intake
    model.setObjective(5*x + 6*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(5*x + 7*y >= 80)
    model.addConstr(3*x + 5*y >= 70)
    model.addConstr(x >= 2*y)

    # Optimize model
    model.optimize()

    # Get the minimum sugar intake
    obj = model.objVal

    return obj