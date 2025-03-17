import gurobipy as gp
from gurobipy import GRB

def prob_140():
    """
    Returns:
        obj: an integer, the minimized total radiation received by the pancreas
    """
    # Create a new model
    model = gp.Model("radiation_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # minutes of Beam 1 used
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # minutes of Beam 2 used

    # Set objective function
    model.setObjective(0.3*x + 0.2*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(0.3*x + 0.2*y <= 0.2, "pancreas_dose")
    model.addConstr(0.2*x + 0.1*y <= 4, "skin_dose")
    model.addConstr(0.6*x + 0.4*y >= 3, "tumor_dose")

    # Optimize the model
    model.optimize()

    # Get the minimized total radiation received by the pancreas
    obj = model.objVal

    return obj