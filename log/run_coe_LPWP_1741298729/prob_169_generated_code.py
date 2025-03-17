import gurobipy as gp
from gurobipy import GRB

def prob_169(camels, horses):
    """
    Args:
        camels: an integer indicating the number of camels
        horses: an integer indicating the number of horses
    Returns:
        obj: an integer, the minimal number of animals
    """
    # Create a new model
    model = gp.Model("animal_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="camels")
    y = model.addVar(vtype=GRB.INTEGER, name="horses")

    # Set objective function: minimize the total number of animals used
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x * 50 >= 1000)
    model.addConstr(y * 60 >= 1000)
    model.addConstr(20 * x + 30 * y <= 450)
    model.addConstr(y <= x)

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj