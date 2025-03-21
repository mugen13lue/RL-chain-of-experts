import gurobipy as gp
from gurobipy import GRB

def prob_168():
    """
    Returns:
        obj: an integer, total number of scooters used
    """
    obj = 0

    # Create a new model
    m = gp.Model("transportation_problem")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # number of scooters used
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # number of rickshaws used

    # Set objective function: minimize the total number of scooters used
    m.setObjective(x, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(2*x + 3*y >= 300, "visitors_constraint")
    m.addConstr(y <= 0.4*(x + y), "rickshaw_limit_constraint")

    # Optimize the model
    m.optimize()

    if m.status == GRB.OPTIMAL:
        obj = x.x

    return obj