import gurobipy as gp
from gurobipy import GRB

def prob_19(thin_jar, stubby_jar):
    """
    Args:
        thin_jar: an integer, the number of thin jars
        stubby_jar: an integer, the number of stubby jars
    Returns:
        obj: an integer, the maximum profit
    """
    # Create a new model
    model = gp.Model("jar_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="thin_jars")
    y = model.addVar(vtype=GRB.INTEGER, name="stubby_jars")

    # Set objective function
    model.setObjective(5*x + 9*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(50*x + 30*y <= 3000, "shaping_time")
    model.addConstr(90*x + 150*y <= 4000, "baking_time")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj