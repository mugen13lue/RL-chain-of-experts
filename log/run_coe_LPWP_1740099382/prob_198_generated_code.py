import gurobipy as gp
from gurobipy import GRB

def prob_198(vans, cars):
    """
    Solve the voter transportation problem.

    Args:
        vans: an integer, number of vans
        cars: an integer, number of cars

    Returns:
        obj: an integer, total number of cars used
    """
    # Create a new model
    model = gp.Model("voter_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="vans")
    y = model.addVar(vtype=GRB.INTEGER, name="cars")

    # Set objective function: minimize the total number of cars used
    model.setObjective(y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(6*x + 3*y >= 200, "transporting_voters")
    model.addConstr(x <= 0.3*(x + y), "limit_on_vans")

    # Optimize model
    model.optimize()

    # Get the total number of cars used
    obj = model.objVal

    return obj