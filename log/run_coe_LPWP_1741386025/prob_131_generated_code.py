import gurobipy as gp
from gurobipy import GRB

def prob_131(bananas, mangoes):
    """
    Args:
        bananas: an integer, number of bananas
        mangoes: an integer, number of mangoes
    Returns:
        obj: an integer, minimum sugar intake
    """
    # Create a new model
    model = gp.Model("gorilla_diet")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="bananas")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="mangoes")

    # Set objective
    model.setObjective(10*x + 8*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(80*x + 100*y >= 4000)
    model.addConstr(20*x + 15*y >= 150)
    model.addConstr(8*y <= 0.33*(8*x + 10*y))

    # Optimize model
    model.optimize()

    # Get the minimum sugar intake
    obj = model.objVal

    return obj