from gurobipy import *

def prob_170(small_suitcases, large_suitcases):
    """
    Args:
        small_suitcases: an integer, the number of small suitcases
        large_suitcases: an integer, the number of large suitcases
    Returns:
        number_of_snacks: an integer, the maximum number of snacks that can be delivered
    """
    m = Model()

    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")
    y = m.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective
    m.setObjective(50*x + 80*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(x >= 2*y)
    m.addConstr(x <= 70)
    m.addConstr(y <= 50)
    m.addConstr(y >= 15)
    m.addConstr(x + y <= 70)

    # Optimize model
    m.optimize()

    # Get the optimal solution
    number_of_snacks = m.objVal

    return number_of_snacks