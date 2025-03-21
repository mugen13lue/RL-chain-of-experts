from gurobipy import *

def prob_168(scooter, rickshaw):
    """
    Args:
        scooter: an integer, number of scooters used
        rickshaw: an integer, number of rickshaws used

    Returns:
        x: an integer, total number of scooters used
    """
    # Create a new model
    m = Model()

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # Number of scooters used
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # Number of rickshaws used

    # Set objective: minimize the total number of scooters used
    m.setObjective(x, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(2*x + 3*y >= 300, "visitor_constraint")
    m.addConstr(y <= 0.4*(x + y), "rickshaw_constraint")

    # Optimize model
    m.optimize()

    if m.status == GRB.OPTIMAL:
        x = int(x.x)

    return x