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
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of vans
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of cars

    # Set objective function: minimize total number of cars used
    model.setObjective(y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(6*x + 3*y >= 200, "min_voters")  # Transport at least 200 voters
    model.addConstr(x <= 0.3*(x + y), "max_vans")  # At most 30% of vehicles can be vans

    # Optimize the model
    model.optimize()

    # Get the total number of cars used
    obj = int(model.objVal)

    return obj