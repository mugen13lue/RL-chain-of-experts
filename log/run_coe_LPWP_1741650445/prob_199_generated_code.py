import gurobipy as gp
from gurobipy import GRB

def prob_199(hamburgers, chicken_wraps):
    """
    Args:
        hamburgers: an integer, representing the number of hamburgers
        chicken_wraps: an integer, representing the number of chicken wraps
    Returns:
        obj: an integer, representing the minimum cost
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="hamburgers")
    y = model.addVar(vtype=GRB.INTEGER, name="chicken_wraps")

    # Set objective function: minimize cost
    model.setObjective(6.5*x + 4*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(800*x + 450*y >= 2200, "Calories")
    model.addConstr(19*x + 12*y >= 50, "Protein")
    model.addConstr(20*x + 10*y >= 70, "Carbs")

    # Optimize model
    model.optimize()

    # Get the minimum cost
    obj = model.objVal

    return obj