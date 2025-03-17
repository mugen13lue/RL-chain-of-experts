import gurobipy as gp
from gurobipy import GRB

def prob_145(process_1, process_2):
    """
    Args:
        process_1: an integer, number of times process 1 should be run
        process_2: an integer, number of times process 2 should be run

    Returns:
        x: an integer, number of hours process 1 should be run
        y: an integer, number of hours process 2 should be run
    """
    model = gp.Model("process_optimization")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(50*x + 60*y <= 2000)
    model.addConstr(35*x + 50*y >= 1200)
    model.addConstr(12*x + 30*y >= 1200)

    # Objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    # Get the optimal values of x and y
    x_opt = round(x.x)
    y_opt = round(y.x)

    return x_opt, y_opt